"use client";

import React, { useEffect, useRef } from 'react';

export const TradingRecord = () => {
  const scrollRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const scrollElement = scrollRef.current;
    if (!scrollElement) return;

    // Auto-scroll function
    const autoScroll = () => {
      const isAtBottom = scrollElement.scrollHeight - scrollElement.scrollTop <= scrollElement.clientHeight + 10;
      
      if (isAtBottom) {
        // If at bottom, immediately return to top
        scrollElement.scrollTo({ top: 0 });
      } else {
        // Continue scrolling down
        scrollElement.scrollBy({ top: 1 });
      }
    };

    // Set scroll interval
    const scrollInterval = setInterval(autoScroll, 50);

    return () => {
      clearInterval(scrollInterval);
    };
  }, []);

  return (
    <div className="w-full h-full relative">
      <h3 className="text-xl font-bold mb-4 text-foreground">Trading Record</h3>
      <div 
        ref={scrollRef}
        className="absolute inset-0 top-12 overflow-y-auto font-mono text-sm text-foreground whitespace-pre px-4 pointer-events-none" 
        style={{ 
          scrollbarWidth: 'none',
          msOverflowStyle: 'none',
          WebkitOverflowScrolling: 'touch'
        }}>
{`=== BTCUSDT Trading Record ===
Start Time: 2025-03-31 11:17:40
Initial Capital: 1,000,000.00

Time            Action  Price       Quantity    Amount      Return Rate
----------------------------------------------------------------------------------------------------

Starting real-time trading BTCUSDT

=== New Prediction Start (Current Time: 2025-03-31 11:17:40) ===
Current Trend: Downward

Prediction Results (Data Time: 2025-03-31 03:15:00):
Current Price: 81595.93
Machine Learning Prediction: 81166.67
Quantum Prediction: 81543.54
I Ching Factor: 0.2441
Diamond Sutra Factor: 0.0400
Comprehensive Prediction: 81355.10
95% Confidence Interval: [81207.48, 81502.73]
--------------------------------------------------
Current Trend: Downward

Prediction Results (Data Time: 2025-03-31 03:15:00):
Current Price: 81595.93
Machine Learning Prediction: 81166.67
Quantum Prediction: 81543.54
I Ching Factor: 0.2441
Diamond Sutra Factor: 0.0400
Comprehensive Prediction: 81355.10
95% Confidence Interval: [81207.48, 81502.73]
--------------------------------------------------

=== BTCUSDT Trading Diagnosis (2025-03-31 11:17:40) ===
Current Price: 81595.93
5-day MA: 81773.27
10-day MA: 81862.80
20-day MA: 81988.94
RSI: 36.15
Bollinger Upper Band: 82611.17
Bollinger Lower Band: 81366.71
Volume Ratio: 0.26

Market Trend Analysis:
Trend Direction: Downward
Trend Strength: Strong
Expected Change: -0.06%
I Ching Factor: 0.2441

Position Information:
Holding Amount: 0.00000000
Available Funds: 1,000,000.00 USDT
Total Asset Value: 1,000,000.00 USDT
--------------------------------------------------

Waiting for next update (599 seconds)...

=== New Prediction Start (Current Time: 2025-03-31 11:27:41) ===
Current Trend: Consolidating

Prediction Results (Data Time: 2025-03-31 03:15:00):
Current Price: 81797.43
Machine Learning Prediction: 81427.02
Quantum Prediction: 81768.02
I Ching Factor: 0.1588
Diamond Sutra Factor: 0.0600
Comprehensive Prediction: 81597.52
95% Confidence Interval: [81445.86, 81749.18]
--------------------------------------------------
=== BTCUSDT Trading Diagnosis (2025-03-31 11:27:41) ===
Current Price: 81797.43
5-day Moving Average: 81813.27
10-day Moving Average: 81882.80
20-day Moving Average: 81998.94
RSI: 39.66
Bollinger Band Upper Limit: 82600.67
Bollinger Band Lower Limit: 81397.20
Volume Ratio: 1.05

Market Trend Analysis:
Trend Direction: Downward
Trend Strength: Strong
Expected Change: -0.04%
I Ching Factor: 0.1588

Position Information:
Holding Quantity: 0.00000000
Available Funds: 1,000,000.00 USDT
Total Asset Value: 1,000,000.00 USDT
Waiting for Next Update (in 599 seconds)...

=== New Forecast Start (Current Time: 2025-03-31 11:37:41) ===
Current Trend: Consolidation

Forecast Results (Data Time: 2025-03-31 03:30:00):
Current Price: 81722.01
Machine Learning Forecast: 81439.99
Quantum Forecast: 81706.44
I Ching Factor: 0.1104
Diamond Sutra Factor: 0.0600
Comprehensive Forecast: 81573.22
95% Confidence Interval: [81414.73, 81731.71]
Current Trend: Consolidation

Forecast Results (Data Time: 2025-03-31 03:30:00):
Current Price: 81722.01
Machine Learning Forecast: 81439.99
Quantum Forecast: 81706.44
I Ching Factor: 0.1104
Diamond Sutra Factor: 0.0600
Comprehensive Forecast: 81573.22
95% Confidence Interval: [81414.73, 81731.71]
=== BTCUSDT Trading Diagnosis (2025-03-31 11:37:41) ===
Current Price: 81722.01
5-day Moving Average: 81818.04
10-day Moving Average: 81865.65
20-day Moving Average: 81959.46
RSI: 40.27
Bollinger Band Upper Limit: 82517.48
Bollinger Band Lower Limit: 81401.44
Volume Ratio: 0.36

Market Trend Analysis:
Trend Direction: Downward
Trend Strength: Moderate
Expected Change: -0.02%
I Ching Factor: 0.1104

Position Information:
Holding Quantity: 0.00000000
Available Funds: 1,000,000.00 USDT
Total Asset Value: 1,000,000.00 USDT
Waiting for Next Update (in 599 seconds)...

=== New Forecast Start (Current Time: 2025-03-31 11:47:42) ===
Current Trend: Consolidation

Forecast Results (Data Time: 2025-03-31 03:45:00):
Current Price: 81647.10
Machine Learning Forecast: 81319.47
Quantum Forecast: 81580.01
I Ching Factor: 0.4096
Diamond Sutra Factor: 0.0460
Comprehensive Forecast: 81449.74
95% Confidence Interval: [81335.38, 81564.11]
Current Trend: Consolidation

Forecast Results (Data Time: 2025-03-31 03:45:00):
Current Price: 81647.10
Machine Learning Forecast: 81319.47
Quantum Forecast: 81580.01
I Ching Factor: 0.4096
Diamond Sutra Factor: 0.0460
Comprehensive Forecast: 81449.74
95% Confidence Interval: [81335.38, 81564.11]
=== BTCUSDT Trading Diagnosis (2025-03-31 11:47:42) ===
Current Price: 81647.10
5-day Moving Average: 81754.26
10-day Moving Average: 81810.52
20-day Moving Average: 81918.62
RSI: 43.54
Bollinger Band Upper Limit: 82447.23
Bollinger Band Lower Limit: 81390.00
Volume Ratio: 0.14

Market Trend Analysis:
Trend Direction: Downward
Trend Strength: Strong
Expected Change: -0.08%
I Ching Factor: 0.4096

Position Information:
Holding Quantity: 0.00000000
Available Funds: 1,000,000.00 USDT
Total Asset Value: 1,000,000.00 USDT
Waiting for Next Update (in 599 seconds)...

=== New Forecast Start (Current Time: 2025-03-31 11:57:42) ===
Current Trend: Consolidation`}
      </div>
    </div>
  );
}; 