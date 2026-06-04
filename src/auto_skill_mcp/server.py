from fastmcp import FastMCP

mcp = FastMCP("auto-skill-mcp")


@mcp.tool()
def ping() -> str:
    """Health check — returns pong if server is running."""
    return "pong"


def main() -> None:
    mcp.run()
