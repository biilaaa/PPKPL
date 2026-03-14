# Week 8 – Automated UI and App Building

## Overview

Pada Week 8 ini saya membangun tiga versi aplikasi web yang sama menggunakan teknologi yang berbeda. Aplikasi yang dibuat adalah TaskFlow, yaitu aplikasi sederhana untuk mengelola daftar tugas (task manager).

Tujuan dari assignment ini adalah untuk memahami bagaimana AI tools dan berbagai stack teknologi dapat mempercepat proses pembuatan aplikasi, khususnya dalam pembangunan UI dan aplikasi end-to-end.

Setiap versi aplikasi memiliki fitur utama yang sama yaitu:

- Create task
- View task list
- Delete task
- Penyimpanan data (database atau local state)

---

# App Concept – TaskFlow

TaskFlow adalah aplikasi task management sederhana yang memungkinkan pengguna mencatat dan mengelola tugas harian.

Fitur utama:

- Menambahkan tugas baru
- Melihat daftar tugas
- Menghapus tugas
- Menyimpan data task

Setiap task memiliki atribut:

- title
- description

Aplikasi ini diimplementasikan menggunakan tiga stack teknologi berbeda untuk melihat perbedaan cara pembangunan aplikasi.

---

# Version 1 – TaskFlow Bolt Stack

Folder:

```
taskflow-bolt
```

Tech Stack:

- React
- Node.js
- Express
- SQLite

Deskripsi:

Versi pertama menggunakan pendekatan AI-assisted development dengan Bolt untuk menghasilkan struktur aplikasi. Aplikasi ini memiliki frontend React dan backend Express yang terhubung dengan database SQLite untuk menyimpan data task.

Fitur:

- Create task
- View task list
- Delete task
- Data tersimpan di SQLite database

Cara menjalankan:

Backend:

```
cd taskflow-bolt/backend
npm install
node server.js
```

Frontend:

```
cd taskflow-bolt/frontend
npm install
npm run dev
```

Buka di browser:

```
http://localhost:5173
```

---

# Version 2 – TaskFlow Flask

Folder:

```
taskflow-flask
```

Tech Stack:

- Python
- Flask
- SQLite
- HTML + CSS

Deskripsi:

Versi kedua menggunakan Flask sebagai backend framework Python. Aplikasi ini menggunakan template HTML sederhana untuk menampilkan UI dan SQLite sebagai database.

Fitur:

- Create task
- View task list
- Delete task
- Data disimpan di SQLite database

Cara menjalankan:

Install dependency:

```
pip install flask
```

Buat database:

```
python init_db.py
```

Jalankan aplikasi:

```
python app.py
```

Buka di browser:

```
http://127.0.0.1:5000
```

---

# Version 3 – TaskFlow Next.js

Folder:

```
taskflow-nextjs
```

Tech Stack:

- Next.js
- React
- TypeScript

Deskripsi:

Versi ketiga menggunakan Next.js framework untuk membangun aplikasi frontend modern berbasis React. Data task disimpan sementara menggunakan state React.

Fitur:

- Create task
- View task list
- Delete task
- UI interaktif menggunakan React state

Cara menjalankan:

```
cd taskflow-nextjs
npm install
npm run dev
```

Buka di browser:

```
http://localhost:3000
```

---

# Project Structure

```
week8
│
├── taskflow-bolt
│
├── taskflow-flask
│
├── taskflow-nextjs
│
├── assignment.md
├── writeup.md
└── README.md
```

---

# Conclusion

Melalui assignment ini saya mempelajari bagaimana aplikasi yang sama dapat dibangun menggunakan **berbagai teknologi dan pendekatan berbeda**.

Perbandingan utama dari ketiga versi:

| Stack      | Karakteristik                                       |
| ---------- | --------------------------------------------------- |
| Bolt Stack | Full-stack JavaScript dengan AI-generated structure |
| Flask      | Backend Python sederhana dengan template HTML       |
| Next.js    | Frontend modern berbasis React framework            |

Setiap stack memiliki kelebihan masing-masing dalam hal kecepatan development, fleksibilitas, dan kompleksitas implementasi.

Assignment ini juga menunjukkan bagaimana AI tools dan framework modern dapat mempercepat proses prototyping UI dan pengembangan aplikasi web.
