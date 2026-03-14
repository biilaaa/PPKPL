# Week 8 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Zahra Nabila \
SUNet ID: - \
Citations: Bolt.new documentation, Next.js documentation, Flask documentation, React documentation

This assignment took me about **TODO** hours to do.

## App Concept

```
Pada assignment ini saya membuat sebuah aplikasi sederhana bernama TaskFlow, yaitu aplikasi task manager yang memungkinkan pengguna untuk mencatat dan mengelola daftar tugas. Aplikasi ini dirancang untuk membantu pengguna menambahkan, melihat, dan menghapus tugas dengan cepat melalui antarmuka web yang sederhana.

Setiap task memiliki atribut dasar seperti title dan description, yang memungkinkan pengguna mencatat informasi singkat tentang pekerjaan yang perlu dilakukan. Aplikasi ini menyediakan fitur utama berupa Create, Read, dan Delete task yang ditampilkan dalam bentuk daftar.

Untuk memahami bagaimana aplikasi yang sama dapat dibangun menggunakan teknologi yang berbeda, TaskFlow diimplementasikan dalam tiga stack yang berbeda, yaitu React + Express (Bolt version), Flask (Python), dan Next.js. Ketiga versi ini memiliki fitur yang sama tetapi menggunakan pendekatan teknologi yang berbeda.
```

## Version #1 Description

```
APP DETAILS:
===============
Folder name: taskflow-bolt
AI app generation platform: Bolt.new
Tech Stack: React, Node.js, Express, SQLite
Persistence: SQLite database
Frameworks/Libraries Used: React, Express, Node.js, SQLite
(Optional but recommended) Screenshots of core flows:

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
Saat menggunakan Bolt, salah satu masalah utama yang muncul adalah keterbatasan environment pada Bolt sandbox yang tidak dapat menjalankan npm install dengan normal. Hal ini menyebabkan dependency seperti Vite tidak dapat diinstall langsung dari Bolt. Untuk mengatasinya, saya menyalin struktur project yang dihasilkan Bolt dan menjalankannya secara lokal menggunakan Node.js di komputer saya.

Selain itu, saya juga harus menyesuaikan beberapa bagian frontend dan backend agar komunikasi antara React frontend dan Express backend dapat berjalan dengan benar melalui API endpoint /tasks.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel):
Prompt yang terlalu kompleks pada Bolt sering menghasilkan konfigurasi tambahan seperti database cloud atau authentication yang tidak diperlukan. Oleh karena itu, prompt yang lebih sederhana seperti task manager CRUD sederhana memberikan hasil yang lebih stabil dan mudah dijalankan.

Secara umum Bolt cukup membantu dalam memberikan struktur awal aplikasi, namun tetap diperlukan penyesuaian manual pada beberapa bagian kode.

c. Approximate time-to-first-run and time-to-feature metrics:
Time to first run: 2 jam
Time to working CRUD features: sekitar 1–2 jam
```

## Version #2 Description

```
APP DETAILS:
===============
Folder name: taskflow-flask
AI app generation platform: Manual implementation (Flask)
Tech Stack: Python, Flask, SQLite, HTML, CSS
Persistence: SQLite database
Frameworks/Libraries Used: Flask, SQLite, Jinja2 Template Engine
(Optional but recommended) Screenshots of core flows:

REFLECTIONS:
===============
a. Issues encountered per stack and how you resolved them:
Pada versi Flask, tantangan utama adalah memastikan struktur folder Flask benar, khususnya penggunaan folder templates untuk HTML dan static untuk file CSS atau JavaScript. Awalnya terjadi error karena file database dan routing tidak berada pada lokasi yang sesuai.

Masalah ini dapat diselesaikan dengan memastikan bahwa file app.py berada pada root folder project dan template HTML berada di dalam folder templates.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel):
Versi Flask tidak menggunakan AI generator secara langsung, sehingga seluruh struktur aplikasi dibuat secara manual. Hal ini memberikan kontrol yang lebih besar terhadap kode, tetapi membutuhkan lebih banyak konfigurasi dibandingkan pendekatan AI-generated project.

c. Approximate time-to-first-run and time-to-feature metrics: TODO
Time to first run: sekitar 10–15 menit
Time to working CRUD features: sekitar 30–45 menit

## Version #3 Description
```

# APP DETAILS:

Folder name: taskflow-nextjs
AI app generation platform: Manual implementation (Next.js)
Tech Stack: Next.js, React, TypeScript
Persistence: React state (temporary storage)
Frameworks/Libraries Used: Next.js, React, TypeScript
(Optional but recommended) Screenshots of core flows: TODO

# REFLECTIONS:

a. Issues encountered per stack and how you resolved them:
Pada versi Next.js, salah satu tantangan adalah memahami struktur App Router yang digunakan oleh Next.js versi terbaru. Awalnya saya mencoba mencari file pages/index.js, namun project menggunakan struktur app/page.tsx.

Solusinya adalah memodifikasi file page.tsx secara langsung dan menambahkan directive "use client" agar React hooks seperti useState dapat digunakan.

b. Prompting (e.g. what required additional guidance; what worked poorly/wel):
Versi Next.js tidak menggunakan AI generator secara langsung, namun struktur awal project dibuat menggunakan CLI create-next-app. Framework ini memudahkan pembuatan aplikasi React modern dengan konfigurasi yang sudah siap digunakan.

c. Approximate time-to-first-run and time-to-feature metrics:
Time to first run: sekitar 30 menit
Time to working CRUD features: sekitar 15 menit
