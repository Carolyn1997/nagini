const StorySection = () => {
  const mcpServers = [
    {
      name: "Solana Agent Kit MCP Server",
      url: "https://github.com/sendaifun/solana-agent-kit/tree/main/examples/agent-kit-mcp-server",
      description: "A Solana Agent Kit implementation using MCP for handling protocol operations on the Solana blockchain. Supports all Solana Agent Kit actions with standardized interactions and environment-based configuration."
    },
    {
      name: "GOAT MCP Server",
      url: "https://github.com/goat-sdk/goat/tree/main/typescript/examples/by-framework/model-context-protocol",
      description: "A GOAT SDK implementation enabling Claude Desktop to send and receive ETH and ERC-20 tokens on EVM networks. Features Base Sepolia support and easy Claude Desktop integration."
    },
    {
      name: "Aldrin Labs Solana MCP Server",
      url: "https://github.com/Aldrin-labs/solana-mcp-server",
      description: "A comprehensive MCP server providing 21 essential Solana RPC methods including account operations, token management, system information, and staking functionality."
    },
    {
      name: "Solana Limit Order MCP Server",
      url: "https://github.com/dimitrov-d/solana-limit-order-mcp",
      description: "An MCP Server providing capabilities to place limit orders on Solana via Jupiter. Enables AI agents to set limit buy/sell orders, view order history, and manage token operations."
    },
    {
      name: "Solana Forum Summarizer MCP Server",
      url: "https://github.com/dimitrov-d/solana-forum-summarizer-mcp",
      description: "Browse and summarize the Solana Forum. Get latest/popular posts, sort by category/author, search by keyword and summarize contents."
    },
    {
      name: "AMOCA MCP Server",
      url: "https://github.com/manolaz/amoca-solana-mcp-server",
      description: "Specialized in Solana wallet analysis with features for token balance analysis, portfolio valuation, and historical transaction review."
    },
    {
      name: "SolMCP Solana MCP Server",
      url: "https://github.com/N-45div/SolMCP---SendAI-MCP-competition",
      description: "A set of 7 tools for Solana degens, validators and node operators using Helius and Dexscrenner with Pyth oracle integration."
    },
    {
      name: "daoCLI MCP Server",
      url: "https://github.com/DaoCLI/daoCLI-init",
      description: "MCP-compatible DAO server for seamless, customizable DAO deployments via CLI. Enables AI-agent developers to embed Solana-based DAOs into apps."
    },
    {
      name: "Hubble MCP Server",
      url: "https://github.com/HubbleVision/hubble-ai-mcp",
      description: "Data analysis and visualization for transactions on pumpfun and DEXs with natural language capabilities."
    },
    {
      name: "Solana DeFi Analytics MCP Server",
      url: "https://github.com/kirtiraj22/solana-mcp",
      description: "Comprehensive analytics and insights for Solana wallets and DeFi interactions. Analyze wallet behavior and optimize DeFi strategies."
    },
    {
      name: "Quant72 MCP",
      url: "https://github.com/Quant72AI/quant72-mcp",
      description: "🚀 All-in-one on-chain quantitative trading expert with multiple market data sources and advanced analytical tools."
    },
    {
      name: "spice MCP Server",
      url: "https://github.com/getnimbus/spice",
      description: "Implements a Solana data query system for fetching catalog metadata and blockchain data via Flipside API."
    },
    {
      name: "Memecoin Observatory MCP",
      url: "https://github.com/tony-42069/solana-mcp.git",
      description: "Analyze memecoins, track trends, and provide AI-powered insights using cultural analysis and on-chain data."
    },
    {
      name: "Solana Wallet Security Scanner",
      url: "https://github.com/mohitparmar1/Solana-Wallet-Security-Scanner",
      description: "Security analysis system for scanning wallets, detecting threats, and monitoring blockchain activity."
    },
    {
      name: "MCP Meme Deployer",
      url: "https://github.com/kirabuilds/mcp-meme-deployer",
      description: "Deploy instantly tradable tokens on Solana at zero cost through simple conversations with Claude Desktop."
    }
  ];

  return (
    <section className="py-8 md:py-12 lg:py-16 bg-background" id="mcp">
      <div className="main-container">
        <div className="text-center mb-8 md:mb-12">
          <h2 className="text-xl md:text-3xl font-bold mb-2 text-[#B7A187]">MCP Servers</h2>
          {/* <h3 className="text-2xl font-bold text-foreground mt-4 lg:mt-8 px-4 lg:px-16">
            Our MCP Server coordinator as an open platform, allowing other developers or traders to access their own AI Agents and form a "market" for trading agents.
          </h3> */}
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-6">
          {mcpServers.map((server, index) => (
            <a 
              key={index}
              href={server.url}
              target="_blank"
              rel="noopener noreferrer"
              className="block p-6 bg-card rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-200 border border-border"
            >
              <h4 className="text-lg font-semibold text-foreground mb-3">{server.name}</h4>
              <p className="text-sm text-muted-foreground line-clamp-2 sm:line-clamp-3 lg:line-clamp-4 xl:line-clamp-5">{server.description}</p>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
};

export default StorySection;
