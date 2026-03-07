🛠️ MCP GitHub Manager - Week 3 Assignment

📌 Description
Proyek ini adalah implementasi dari Model Context Protocol (MCP) server yang menghubungkan AI Agent (seperti Claude Desktop) dengan GitHub API. Server ini memungkinkan AI untuk melakukan navigasi kode dan manajemen issues secara otonom dan terstruktur .

🚀 Features (Tools)
Berdasarkan prinsip Context Engineering, server ini mengekspos dua tools spesifik agar AI dapat bekerja secara efisien tanpa menghabiskan ruang konteks:
• get_repo_issues: Mengambil daftar semua issues yang terbuka di repositori tertentu.
• add_comment_to_issue: Menambahkan komentar baru pada issue spesifik untuk mempercepat alur kerja kolaborasi.

Setup & Installation

1. Prerequisites
   • Python 3.10 atau versi di atasnya.
   • GitHub Personal Access Token (PAT) dengan izin akses repo.
2. Clone & Install
   Bash
   cd week3
   pip install -r requirements.txt
3. Environment Variables
   Buat file .env di dalam folder server/ dan tambahkan token kamu:
   Cuplikan kode
   GITHUB_TOKEN=ghp_MasukanTokenKamuDisini

Usage Example
Setelah terhubung, kamu bisa memberikan instruksi kepada AI seperti:
• "Tolong cek daftar issue di repo biilaaa/PPKPL."
• "Berikan komentar 'Terima kasih, akan segera saya cek' pada issue nomor 5 di repo tersebut."

 
Reliability & Resilience
• Error Handling: Menggunakan blok try-except untuk menangani kegagalan HTTP dan timeout dari API GitHub .
• Context Management: Tool didesain secara spesifik untuk mengembalikan data yang difilter guna mencegah Context Distraction pada model AI.
