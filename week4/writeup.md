# Week 4 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Zahra Nabila \
SUNet ID: 2310817320007 \
Citations: Boris Cherny (SubAgents & Best Practices), Anthropic Documentation.

This assignment took me about **TODO** hours to do.

## YOUR RESPONSES

### Automation #1

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)

> Terinspirasi dari praktik Security Engineering di Anthropic yang menekankan pengurangan beban manual melalui skrip otomatis untuk menjaga konsistensi antara kode dan dokumentasi.

b. Design of each automation, including goals, inputs/outputs, steps

> Goal: Mencegah documentation drift antara router backend dan file Markdown.

Inputs: File Python di backend/app/routers/.

Outputs: Tabel API yang diperbarui di docs/API.md.

Steps: Skrip memindai dekorator @router menggunakan modul ast, mengekstrak metadata, dan menulis ulang tabel dokumentasi secara otomatis.

c. How to run it (exact commands), expected outputs, and rollback/safety notes

> Command: python scripts/sync_api.py

Expected Output: Pesan "API documentation updated successfully!" di terminal.

Safety: Skrip hanya melakukan operasi tulis pada file .md yang spesifik dan tidak mengubah logika kode inti.

d. Before vs. after (i.e. manual workflow vs. automated workflow)

> Manual: Pengembang harus menulis manual setiap endpoint baru di Markdown, yang seringkali terlupakan (outdated).

Automated: Dokumentasi selalu sinkron 100% dengan kondisi kode terbaru hanya dengan satu perintah.

e. How you used the automation to enhance the starter application

> Saya menggunakannya untuk memastikan field priority yang baru saya tambahkan langsung tercatat di dokumentasi teknis tanpa kesalahan ketik manual.

### Automation #2

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)

> Mengikuti pola Multi-Agent Orchestration dan SubAgents dari Boris Cherny, di mana tugas dibagi menjadi peran spesifik (Architect, Tester, Coder) untuk meningkatkan keandalan.

b. Design of each automation, including goals, inputs/outputs, steps

> Goal: Menjamin setiap fitur baru memiliki unit test yang valid sebelum diimplementasikan.

Inputs: Instruksi di CLAUDE.md dan prompt dari pengembang.

Outputs: Kode yang teruji (robust) dan lolos pytest.

Steps: Membuat failing test -> Implementasi kode -> Verifikasi lewat Agentic Loop.

c. How to run it (exact commands), expected outputs, and rollback/safety notes

> Command: $env:PYTHONPATH = "."; pytest -v backend/tests/test_priority.py

Expected Output: Status PASSED pada semua test case.

Safety: Menggunakan database sementara (tempfile) untuk pengujian agar tidak merusak data produksi.

d. Before vs. after (i.e. manual workflow vs. automated workflow)

> Manual: Penambahan fitur dilakukan langsung di kode utama, sering menyebabkan bug yang tidak terdeteksi.

Automated: Fitur baru dipastikan bekerja melalui pengujian otomatis sebelum digabungkan ke sistem utama.

e. How you used the automation to enhance the starter application

> Saya menggunakan alur ini untuk menambah fitur Task Priority (Low, Medium, High). AI bertindak sebagai Tester untuk membuat skenario uji, lalu sebagai Coder untuk memenuhi standar pengujian tersebut.
