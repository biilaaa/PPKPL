from mcp.server.fastmcp import FastMCP
from tools import fetch_github_issues, post_issue_comment

# Buat instance FastMCP
mcp = FastMCP("GitHub-Manager-Billa")

# Daftarkan Tool 1: Membaca Issues
@mcp.tool()
async def get_repo_issues(owner: str, repo: str):
    """Mengambil daftar semua issue yang terbuka di repositori GitHub tertentu."""
    return await fetch_github_issues(owner, repo)

# Daftarkan Tool 2: Memberi Komentar
@mcp.tool()
async def add_comment_to_issue(owner: str, repo: str, issue_number: int, comment_body: str):
    """Menuliskan komentar pada issue GitHub berdasarkan nomor issue-nya."""
    return await post_issue_comment(owner, repo, issue_number, comment_body)

if __name__ == "__main__":
    mcp.run(transport="stdio")