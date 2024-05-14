from crewai_tools import tool

@tool("Check Balance Tool")
def check_balance_tool(dummy_arg=None) -> str:
    """Check the STX balance of the configured wallet."""
    try:
        #return BunScriptRunner.bun_run("wallet", "get-wallet-balance.ts")
        return 1000
    except SyntaxError:
        return "Error: Invalid syntax in mathematical expression"

@tool("Purchase NFT Tool")
def make_purchase_tool(id:str) -> str:
    """Send a transaction to buy the NFT."""
    try:
        #return BunScriptRunner.bun_run("wallet", "get-wallet-balance.ts")
        return 'pending'
    except SyntaxError:
        return "Error: Invalid syntax in mathematical expression"
