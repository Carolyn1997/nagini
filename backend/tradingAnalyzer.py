import time
import requests
import base64
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from openai import OpenAI


class OKXKlineData:
    def __init__(self):
        self.base_url = "https://www.okx.com/api/v5/market/candles"
        self.limit = 100  # 每次请求的最大K线数量

    def get_kline_data(self, symbol, timeframe, limit=1000):
        """
        获取OKX交易所的K线数据

        :param symbol: 交易对，例如 'BTC-USDT'
        :param timeframe: K线时间周期，例如 '1H' 表示1小时
        :param limit: 获取的K线数量，最大为1000
        :return: K线数据列表（仅包含需要的6列）
        """
        all_data = []
        after = None  # 用于分页的时间戳

        while len(all_data) < limit:
            params = {
                'instId': symbol,
                'bar': timeframe,
                'limit': min(self.limit, limit - len(all_data))
            }
            if after:
                params['after'] = after

            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                if data['code'] == '0':
                    klines = data['data']
                    if not klines:
                        break  # 如果没有更多数据，退出循环

                    # 只提取需要的6列数据
                    for kline in klines:
                        filtered_kline = [
                            kline[0],  # timestamp
                            kline[1],  # open
                            kline[2],  # high
                            kline[3],  # low
                            kline[4],  # close
                            kline[5],  # volume
                        ]
                        all_data.append(filtered_kline)

                    after = klines[-1][0]  # 更新分页时间戳
                else:
                    print(f"Error: {data['msg']}")
                    break
            else:
                print(f"Failed to retrieve data: {response.status_code}")
                break
        kline_data = all_data[::-1]

        columns = ['时间', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = pd.DataFrame(kline_data, columns=columns)
        df['时间'] = pd.to_datetime(df['时间'].astype(int), unit='ms')
        df[['Open', 'High', 'Low', 'Close', 'Volume']] = df[[
            'Open', 'High', 'Low', 'Close', 'Volume']].astype(float)

        return df


class TradingAnalyzer:
    def __init__(self, api_key, symbol, period='1H', KLineCnt=500):
        """
        初始化交易分析器
        :param api_key: OpenAI API密钥
        """
        self.client = OpenAI(
            base_url="https://api.gptsapi.net/v1",
            api_key=api_key
        )
        self.symbol = symbol
        self.period = period
        self.KLineCnt = KLineCnt

    def load_data(self):
        """
        加载并预处理CSV数据
        """

        OkxData = OKXKlineData()
        self.df = OkxData.get_kline_data(
            self.symbol, self.period, self.KLineCnt)
        self._calculate_indicators()

    def _calculate_rsi(self, data, window=14):
        """计算RSI指标"""
        delta = data.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=window, min_periods=1).mean()
        avg_loss = loss.rolling(window=window, min_periods=1).mean()
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def _calculate_macd(self, data, fast_period=12, slow_period=26, signal_period=9):
        """计算MACD指标"""
        fast_ema = data.ewm(span=fast_period, adjust=False).mean()
        slow_ema = data.ewm(span=slow_period, adjust=False).mean()
        dif = fast_ema - slow_ema
        dea = dif.ewm(span=signal_period, adjust=False).mean()
        macd = dif - dea
        return dif, dea, macd

    def _calculate_indicators(self):
        """计算所有技术指标"""
        self.df['RSI'] = self._calculate_rsi(self.df['Close'])
        self.df['DIF'], self.df['DEA'], self.df['MACD'] = self._calculate_macd(
            self.df['Close'])

    def create_chart(self):
        """创建图表"""
        # 创建子图布局
        self.fig = make_subplots(
            rows=3, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.1,
            subplot_titles=("K线图", "RSI 曲线", "MACD 曲线"),
            row_heights=[0.4, 0.2, 0.4]
        )

        # 添加K线图
        self._add_candlestick()
        # 添加箱体图
        self._add_box_patterns()
        # 添加RSI
        self._add_rsi()
        # 添加MACD
        self._add_macd()

        # 设置图表样式
        self.fig.update_layout(
            title=f"OKX: {self.symbol} {self.period} KLine.",
            xaxis_title="时间",
            xaxis_rangeslider_visible=False,
            template="plotly_dark",
            height=900,
            showlegend=True,
        )

    def _add_candlestick(self):
        """添加K线图"""
        self.fig.add_trace(go.Candlestick(
            x=self.df.index,
            open=self.df["Open"],
            high=self.df["High"],
            low=self.df["Low"],
            close=self.df["Close"],
            name="K线",
            increasing_line_color='red',
            decreasing_line_color='green'
        ), row=1, col=1)

    def _add_box_patterns(self, N=20):
        """添加箱体图"""
        for i in range(0, len(self.df), N * 2):
            sub_df = self.df.iloc[i:i+N]
            if len(sub_df) < N:
                break

            box_high = sub_df["High"].max()
            box_low = sub_df["Low"].min()
            box_mid = (box_high + box_low) / 2
            start_time = sub_df.index[0]
            end_time = sub_df.index[-1]

            # 添加箱体
            self.fig.add_shape(
                type="rect",
                x0=start_time, x1=end_time,
                y0=box_low, y1=box_high,
                line=dict(color="blue", width=2),
                fillcolor="rgba(0, 150, 255, 0.3)",
                row=1, col=1
            )

            # 添加中线
            self.fig.add_shape(
                type="line",
                x0=start_time, x1=end_time,
                y0=box_mid, y1=box_mid,
                line=dict(color="red", width=1, dash="dot"),
                row=1, col=1
            )

            # 添加价格标注
            for price, y in [(box_high, box_high), (box_low, box_low)]:
                self.fig.add_annotation(
                    x=end_time, y=y,
                    text=f"{price:.2f}",
                    showarrow=False,
                    font=dict(size=12, color="white"),
                    bgcolor="blue",
                    borderpad=4,
                    row=1, col=1
                )

    def _add_rsi(self):
        """添加RSI指标"""
        self.fig.add_trace(go.Scatter(
            x=self.df.index, y=self.df['RSI'],
            mode='lines', name='RSI',
            line=dict(color='blue', width=2)
        ), row=2, col=1)

        # 添加超买超卖线
        for level, name, color in [(70, '超买线 (70)', 'red'), (30, '超卖线 (30)', 'green')]:
            self.fig.add_trace(go.Scatter(
                x=self.df.index,
                y=[level] * len(self.df),
                mode='lines',
                name=name,
                line=dict(color=color, dash='dash')
            ), row=2, col=1)

    def _add_macd(self):
        """添加MACD指标"""
        # 添加DIF和DEA线
        for name, data, color in [('DIF', self.df['DIF'], 'blue'),
                                  ('DEA', self.df['DEA'], 'red')]:
            self.fig.add_trace(go.Scatter(
                x=self.df.index,
                y=data,
                mode='lines',
                name=name,
                line=dict(color=color, width=2)
            ), row=3, col=1)

        # 添加MACD柱状图
        self.fig.add_trace(go.Bar(
            x=self.df.index,
            y=self.df['MACD'],
            name='MACD',
            marker=dict(color=self.df['MACD'].apply(
                lambda x: 'green' if x >= 0 else 'red'
            ))
        ), row=3, col=1)

    def save_chart(self, file_path="photo/chart.png"):
        """保存图表为本地文件"""
        img_bytes = pio.to_image(
            self.fig, format="png", width=1920, height=1080, scale=2)
        with open(file_path, "wb") as f:
            f.write(img_bytes)
        print(f"图表已保存为 {file_path}")

    def get_gpt_analysis(self):
        """获取GPT分析结果"""
        try:
            img_bytes = pio.to_image(
                self.fig, format="png", width=1920, height=1080, scale=2)
            img_base64 = base64.b64encode(img_bytes).decode("utf-8")

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a professional financial analyst and trading expert. Your task is to analyze the given TradingView-style candlestick chart "
                        "and provide an insightful yet engaging trading report. Use relevant indicators such as RSI, MACD, MA, and EMA. "
                        "Format the response in a social media-friendly style, suitable for Twitter/X. "
                        "Make it concise, fun, and engaging, using finance-related memes and trader slang to maximize engagement."
                    )
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Analyze the following TradingView candlestick chart and generate a tweet-style trading report. "
                                "Make sure to include:\n"
                                "1. **Market Overview**: Is it bullish, bearish, or ranging?\n"
                                "2. **Technical Indicators Analysis**:\n"
                                "   - RSI (Is the market overbought or oversold?)\n"
                                "   - MACD (Bullish or bearish crossover?)\n"
                                "   - MA & EMA (Potential support/resistance levels?)\n"
                                "3. **Trade Recommendation**:\n"
                                "   - Suggested **entry price** and **exit price**\n"
                                "   - Risk management strategy (stop-loss & take-profit levels)\n"
                                "4. **Sentiment & Meme Commentary**:\n"
                                "   - Use trader memes to match the trend (🚀 for bullish, 💀 for bearish, 🤡 for sideways)\n"
                                "   - Write it in a fun, engaging tone for social media\n"
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_base64}"
                            }
                        }
                    ]
                }
            ]

            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=260
            )

            return response.choices[0].message.content
        except Exception as e:
            print(f"分析过程中出现错误: {e}")
            return None

    def analyze(self, show_chart=True):
        """
        主要分析函数
        :param csv_file: CSV文件路径
        :param show_chart: 是否显示图表
        :return: GPT分析结果
        """
        self.load_data()
        self.create_chart()

        if show_chart:
            timestamp = int(time.time())
            chart_file = f"photo/{self.symbol}_{timestamp}.png"
            self.save_chart(chart_file)

        return chart_file, self.get_gpt_analysis()

    def check_available_models(self):
        """查看可用的模型列表"""
        try:
            models = self.client.models.list()
            print("可用的模型列表：")
            for model in models:
                print(f"- {model.id}")
        except Exception as e:
            print(f"获取模型列表时出错: {e}")


# # 初始化分析器（需要OpenAI API密钥）
# api_key = "sk-TJif0c2b03e98fe768213a54ea7e175ffe83ad6380afrRHS"
# analyzer = TradingAnalyzer(api_key,"LTC-USDT",'1H',500)
# png_file, analysis_result = analyzer.analyze(show_chart=True)

# # 打印GPT的分析结果
# print(png_file)
# print(analysis_result)
