# Developer Command Center Context Guide

## 🛠 Build & Run Commands

- [cite_start]**Run Application**: `make run` [cite: 512]
- [cite_start]**Run Tests**: `make test` [cite: 512]
- [cite_start]**Linting**: `make lint` [cite: 512]
- [cite_start]**Formatting**: `make format` [cite: 512]

## 📂 Project Structure & Entry Points

- [cite_start]**API Routers**: Terletak di `backend/app/routers/` (seperti `action_items.py` dan `notes.py`). [cite: 462, 466]
- [cite_start]**Data Schemas**: Terletak di `backend/app/schemas.py`. [cite: 490]
- [cite_start]**Database Models**: Terletak di `backend/app/models.py`. [cite: 490]
- [cite_start]**Services/Logic**: Terletak di `backend/app/services/`. [cite: 463]
- [cite_start]**Tests**: Terletak di `backend/tests/`. [cite: 512]

## 🎨 Style & Safety Guardrails

- [cite_start]Sebelum melakukan commit atau mengakhiri sesi, **wajib** menjalankan `make format` dan `make lint`. [cite: 116, 512]
- [cite_start]Selalu gunakan _type hints_ yang ketat pada setiap fungsi baru. [cite: 425]
- [cite_start]Gunakan `black` dan `ruff` sesuai konfigurasi proyek untuk menjaga konsistensi. [cite: 512]

## 🔄 Workflow Expectations

- [cite_start]**Test-Driven Development**: Setiap kali diminta menambah fitur atau memperbaiki bug, buatlah _test case_ baru di `backend/tests/` terlebih dahulu sebelum menulis kode implementasi. [cite: 116, 1518, 1542]
- [cite_start]**Context Awareness**: Selalu baca file `docs/TASKS.md` untuk memahami prioritas pekerjaan saat ini. [cite: 110, 129]
- [cite_start]**Incremental Progress**: Implementasikan perubahan secara bertahap dan lakukan _checkpoint_ (commit) setiap kali satu unit logika selesai. [cite: 1785, 1796]
