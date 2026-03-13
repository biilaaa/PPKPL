# Week 5 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Zahra Nabila \
SUNet ID: - \
Citations: Warp University documentation, Warp AI agent interface

This assignment took me about 2 hours to do.

## YOUR RESPONSES

### Automation A: Warp Drive saved prompts, rules, MCP servers

a. Design of each automation, including goals, inputs/outputs, steps

> Automation yang dibuat pada eksperimen ini adalah Week5 QA Automation menggunakan Warp Drive saved prompt. Tujuan dari automation ini adalah untuk menjalankan proses pengecekan kualitas kode secara otomatis pada proyek FastAPI. Automation ini dirancang untuk membantu developer menjalankan beberapa langkah penting seperti testing, formatting, dan lint checking dalam satu workflow otomatis.

Input dari automation ini adalah proyek FastAPI yang sedang dikerjakan pada direktori project. Output dari automation ini adalah hasil eksekusi beberapa command quality assurance seperti hasil unit test, hasil formatting kode, serta hasil lint checking.

Automation menjalankan beberapa langkah utama yaitu:
pytest - untuk mengeksekusi unit tests yang ada pada proyek
black - untuk melakukan formatting kode agar mengikuti standar penulisan Python
ruff - ntuk melakukan lint checking sehingga potensi kesalahan kode dapat dideteksi lebih awal.

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> Sebelum menggunakan Warp automation, developer harus menjalankan setiap command secara manual di terminal. Proses tersebut melibatkan beberapa langkah seperti menjalankan pytest untuk testing, menjalankan black untuk formatting, dan menjalankan ruff untuk lint checking. Workflow manual ini membutuhkan beberapa command terpisah dan berpotensi menimbulkan kesalahan apabila developer lupa menjalankan salah satu langkah.

Setelah menggunakan Warp automation, workflow tersebut dapat dijalankan melalui satu automation prompt. Warp agent kemudian menjalankan setiap langkah sebagai task workflow secara otomatis. Hal ini membuat proses pengecekan kualitas kode menjadi lebih cepat, lebih konsisten, dan mengurangi kemungkinan kesalahan manusia.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> Automation ini menggunakan semi-autonomous execution. Warp agent dapat menjalankan beberapa command secara otomatis berdasarkan prompt yang diberikan oleh pengguna. Namun, sebelum menjalankan command tertentu, Warp tetap meminta konfirmasi dari pengguna untuk memastikan bahwa command tersebut aman untuk dijalankan.

Pendekatan ini memberikan keseimbangan antara otomatisasi dan kontrol dari developer. Developer tetap dapat memonitor command yang akan dijalankan oleh agent dan memberikan persetujuan sebelum eksekusi dilakukan. Dengan cara ini, automation tetap aman sekaligus meningkatkan efisiensi workflow.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> Pada automation ini tidak digunakan multi-agent workflow secara langsung karena automation ini hanya menjalankan serangkaian command quality assurance secara berurutan. Semua tugas dijalankan oleh satu agent yang mengeksekusi workflow berdasarkan prompt automation yang telah dibuat.

Namun, Warp tetap menggunakan mekanisme task workflow untuk mengorganisasi setiap langkah yang dijalankan oleh agent sehingga proses automation tetap terstruktur.

e. How you used the automation (what pain point it resolves or accelerates)

> Automation ini membantu mengatasi masalah workflow developer yang sering kali harus menjalankan beberapa command secara manual untuk memeriksa kualitas kode. Tanpa automation, developer harus mengingat dan menjalankan setiap command secara terpisah, yang dapat memakan waktu dan berpotensi menimbulkan kesalahan.

Dengan Warp automation, proses ini dapat dijalankan melalui satu prompt sehingga mempercepat proses development workflow. Automation ini sangat berguna terutama ketika developer ingin memastikan bahwa kode sudah lulus testing, formatting, dan lint checking sebelum melakukan commit atau deployment.

### Automation B: Multi‑agent workflows in Warp

a. Design of each automation, including goals, inputs/outputs, steps

> Pada bagian ini digunakan multi-agent workflow yang melibatkan dua agent dengan peran yang berbeda. Tujuan dari eksperimen ini adalah untuk menunjukkan bagaimana beberapa agent dapat bekerja secara paralel untuk membantu proses pengembangan perangkat lunak.

Agent pertama berperan sebagai backend engineer yang bertugas menganalisis struktur API pada proyek FastAPI. Agent ini membaca struktur router, endpoint, schema, dan model yang ada pada proyek kemudian memberikan rekomendasi perbaikan pada desain API seperti penambahan pagination, filtering parameter, serta perbaikan desain endpoint agar lebih sesuai dengan prinsip REST API.

Agent kedua berperan sebagai QA engineer yang bertugas menghasilkan unit test menggunakan pytest. Agent ini membaca struktur endpoint pada proyek kemudian menghasilkan test cases yang lebih komprehensif untuk endpoint notes dan action-items. Setelah menghasilkan test cases, agent juga mencoba menjalankan pytest untuk memverifikasi bahwa test dapat dijalankan dengan benar.

b. Before vs. after (i.e. manual workflow vs. automated workflow)

> Sebelum menggunakan multi-agent workflow, developer biasanya harus melakukan beberapa tugas secara manual seperti menganalisis desain API dan menulis unit test secara terpisah. Proses ini membutuhkan waktu yang cukup lama karena developer harus membaca kode terlebih dahulu sebelum melakukan analisis atau menulis test.

Dengan menggunakan Warp multi-agent workflow, tugas tersebut dapat dilakukan oleh beberapa agent secara paralel. Satu agent dapat melakukan analisis arsitektur API sementara agent lainnya dapat menghasilkan unit test secara otomatis. Hal ini membantu mempercepat proses development dan memungkinkan developer untuk fokus pada tugas yang lebih kompleks.

c. Autonomy levels used for each completed task (what code permissions, why, and how you supervised)

> Multi-agent workflow ini juga menggunakan pendekatan semi-autonomous execution. Warp agent memiliki kemampuan untuk membaca struktur proyek, menghasilkan kode, serta menjalankan command tertentu seperti pytest. Namun, Warp tetap meminta konfirmasi sebelum menjalankan command tertentu untuk memastikan keamanan eksekusi command.

Selama eksperimen ini, developer tetap memonitor aktivitas agent dan memberikan persetujuan sebelum command dijalankan. Hal ini memastikan bahwa automation tetap berada di bawah kontrol pengguna.

d. (if applicable) Multi‑agent notes: roles, coordination strategy, and concurrency wins/risks/failures

> Dalam eksperimen ini, dua agent digunakan dengan peran yang berbeda. Agent pertama berperan sebagai backend engineer yang melakukan analisis desain API, sedangkan agent kedua berperan sebagai QA engineer yang menghasilkan unit tests. Kedua agent bekerja pada task yang berbeda sehingga tidak saling mengganggu.

Pendekatan ini menunjukkan bagaimana beberapa agent dapat bekerja secara paralel untuk menyelesaikan tugas yang berbeda dalam proses pengembangan perangkat lunak. Salah satu keuntungan dari pendekatan ini adalah peningkatan produktivitas karena beberapa tugas dapat dikerjakan secara bersamaan.

Namun, penggunaan multi-agent workflow juga memiliki potensi risiko seperti konflik perubahan kode atau eksekusi command yang tidak diinginkan. Oleh karena itu, pengawasan dari developer tetap diperlukan untuk memastikan bahwa workflow berjalan dengan aman.

e. How you used the automation (what pain point it resolves or accelerates)

> Multi-agent workflow membantu mempercepat proses pengembangan dengan membagi tugas menjadi beberapa bagian yang dapat dikerjakan secara paralel. Dalam eksperimen ini, satu agent digunakan untuk melakukan analisis arsitektur API sementara agent lainnya digunakan untuk menghasilkan unit test.

Pendekatan ini membantu mengurangi beban kerja developer karena beberapa tugas dapat diotomatisasi oleh agent. Dengan bantuan AI agent di Warp, developer dapat menyelesaikan beberapa pekerjaan seperti analisis kode dan pembuatan unit test dengan lebih cepat.

### (Optional) Automation C: Any Additional Automations

Tidak ada automation tambahan yang diimplementasikan pada eksperimen ini karena fokus utama assignment adalah mengeksplorasi penggunaan Warp Drive automation dan multi-agent workflow.
