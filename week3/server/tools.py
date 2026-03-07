import httpx
import os
import logging
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com"

# Setup logging ke stderr (jangan ke stdout agar tidak merusak protokol)
logger = logging.getLogger(__name__)

async def fetch_github_issues(owner: str, repo: str):
    """Mengambil daftar issue dari repositori GitHub tertentu."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/repos/{owner}/{repo}/issues", headers=headers, timeout=10.0)
            response.raise_for_status() # Menangani error HTTP secara otomatis [cite: 405]
            return response.json()
        except httpx.HTTPStatusError as e:
            return f"Error: API GitHub merespons dengan status {e.response.status_code}"
        except Exception as e:
            return f"Terjadi kesalahan teknis: {str(e)}"

async def post_issue_comment(owner: str, repo: str, issue_number: int, body: str):
    """Menambahkan komentar baru pada issue GitHub."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"body": body}
    async with httpx.AsyncClient() as client:
        try:
            url = f"{BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}/comments"
            response = await client.post(url, headers=headers, json=data, timeout=10.0)
            response.raise_for_status()
            return {"status": "success", "message": "Komentar berhasil diposting!"}
        except Exception as e:
            return f"Gagal memposting komentar: {str(e)}"