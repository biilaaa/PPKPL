# Week 6 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Zahra Nabila \
SUNet ID: - \
Citations: Semgrep Documentation dan materi AI Testing and Security

This assignment took me about 1 hours to do.

## Brief findings overview

> Pada tugas ini saya menggunakan Semgrep untuk melakukan static analysis terhadap aplikasi FastAPI yang terdapat pada folder week6. Proses scanning dilakukan menggunakan rules dari Semgrep registry dengan konfigurasi security-audit.

Hasil scanning awal menunjukkan beberapa potensi kerentanan keamanan pada endpoint debugging yang terdapat di backend aplikasi. Kerentanan yang ditemukan berkaitan dengan penggunaan fungsi berbahaya seperti eval(), penggunaan subprocess.run() dengan parameter shell=True, serta penggunaan urllib.request.urlopen() dengan input yang berasal dari pengguna.

Kerentanan tersebut dapat menyebabkan berbagai risiko keamanan seperti code injection, command injection, serta akses tidak sah terhadap sumber daya server. Oleh karena itu, dilakukan beberapa perbaikan pada kode untuk menghilangkan potensi eksploitasi tersebut. Setelah perbaikan dilakukan, proses scanning Semgrep dijalankan kembali dan menunjukkan bahwa tidak ada lagi temuan kerentanan keamanan.

## Fix #1

a. File and line(s)

> week6/backend/app/routers/notes.py dan baris 113-138

b. Rule/category Semgrep flagged

> python.lang.security.audit.eval-detected

c. Brief risk description

> Penggunaan fungsi eval() memungkinkan eksekusi kode Python secara langsung dari input yang diberikan oleh pengguna. Jika input tersebut berasal dari sumber eksternal, maka attacker dapat menjalankan kode berbahaya pada server.

d. Your change (short code diff or explanation, AI coding tool usage)

> Sebelumnya kode menggunakan result = str(eval(expr)) Kode tersebut kemudian diganti dengan menjadi result = str(safe_eval(expr)) yang menggunakan modul ast untuk memproses ekspresi secara lebih aman.

e. Why this mitigates the issue

> Dengan menghapus penggunaan eval() secara langsung dan menggantinya dengan fungsi evaluasi yang lebih terbatas, risiko eksekusi kode arbitrer dapat dihindari.

## Fix #2

a. File and line(s)

> week6/backend/app/routers/notes.py dan baris 140-160

b. Rule/category Semgrep flagged

> python.lang.security.audit.subprocess-shell-true

c. Brief risk description

> Penggunaan subprocess.run() dengan parameter shell=True memungkinkan attacker untuk menyisipkan perintah tambahan ke dalam shell command yang dijalankan oleh aplikasi.

d. Your change (short code diff or explanation, AI coding tool usage)

> Sebelumnya kode menggunakan completed = subprocess.run(cmd, shell=True, capture_output=True, text=True) Kode diperbaiki menjadi completed = subprocess.run(cmd.split(), shell=False, capture_output=True, text=True

e. Why this mitigates the issue

> Dengan menghilangkan penggunaan shell=True, perintah tidak lagi dijalankan melalui shell interpreter sehingga potensi command injection dapat diminimalkan.

## Fix #3

a. File and line(s)

> week6/backend/app/routers/notes.py dan baris 164-172

b. Rule/category Semgrep flagged

> python.lang.security.audit.dynamic-urllib-use-detected

c. Brief risk description

> Penggunaan urllib.request.urlopen() dengan parameter URL yang berasal dari input pengguna dapat memungkinkan attacker untuk mengakses sumber daya lokal server menggunakan skema seperti file://.

d. Your change (short code diff or explanation, AI coding tool usage)

> Sebelumnya kode menggunakan:
> from urllib.request import urlopen
> with urlopen(url) as res:
> Kode kemudian diganti menggunakan library requests:
> import requests
> res = requests.get(url, timeout=5)

e. Why this mitigates the issue

> Library requests hanya mendukung protokol HTTP dan HTTPS sehingga mengurangi risiko akses file lokal atau protokol berbahaya lainnya.
