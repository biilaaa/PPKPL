# Intent

Otomatisasi sinkronisasi antara route API di kode backend dengan dokumentasi teknis.

# Usage

Ketik `/sync-docs` untuk memperbarui docs/API.md.

# Steps

1. Pindai folder `backend/app/routers/` untuk mencari semua fungsi yang menggunakan dekorator `@router.get`, `@router.post`, `@router.put`, atau `@router.delete`.
2. Ekstrak informasi berupa: Method, Endpoint path, dan deskripsi singkat dari _docstring_ fungsi tersebut.
3. Baca file `docs/API.md`.
4. Perbarui tabel daftar API di dalam `docs/API.md` agar sesuai dengan kondisi kode saat ini.
5. Jika ada endpoint baru yang belum didokumentasikan, tambahkan ke dalam daftar TODO di bagian bawah file tersebut.
6. Tampilkan ringkasan perubahan yang telah dilakukan (misal: "Menambahkan 2 endpoint baru ke docs/API.md").
