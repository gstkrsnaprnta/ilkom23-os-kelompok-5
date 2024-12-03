Cara Kerja Daemon
1. Inisialisasi:
   Daemon biasanya dimulai oleh sistem saat booting atau melalui perintah manual. Pada sistem berbasis Unix, daemon sering kali diinisialisasi oleh 'init' atau 'systemd'.
2. Pengalihan Input/Output:
   Setelah daemon dimulai, ia mengalihkan input dan output standar (stdin, stdout, stderr) ke '/dev/null' atau file log. Ini memastikan bahwa daemon tidak terikat pada terminal mana pun dan dapat beroperasi di latar belakang.
3. Forking dan Daemonization:
   Proses daemon sering kali melakukan forking, di mana proses utama menciptakan child process. Proses utama kemudian keluar, sementara child process terus berjalan sebagai daemon.
4. Pengelolaan Tugas:
   Daemon sering kali memiliki loop utama yang terus berjalan, menunggu permintaan atau tugas yang harus diproses. Misalnya, daemon web akan menunggu permintaan HTTP dari klien.
5. Menangani Sinyal:
   Daemon harus dapat menangani sinyal dari sistem operasi, seperti sinyal untuk menghentikan atau memulai ulang proses. Ini dilakukan dengan menetapkan handler yang sesuai untuk sinyal yang relevan.
6. Monitoring dan Logging:
   Banyak daemon dilengkapi dengan mekanisme untuk memantau kinerja dan mencatat aktivitas ke dalam file log. Ini membantu dalam pemecahan masalah dan pemeliharaan sistem.

Manfaat Daemon
1. Automatisasi Tugas:
   Daemon memungkinkan otomatisasi berbagai tugas, seperti pencadangan data, pemantauan sistem, dan pengelolaan jaringan, sehingga mengurangi beban kerja administrator.
2. Efisiensi Sumber Daya:
   Dengan menjalankan proses di latar belakang, daemon dapat mengoptimalkan penggunaan sumber daya sistem, memungkinkan aplikasi lain untuk berjalan lebih lancar.
3. Layanan Berkelanjutan:
   Daemon dapat menyediakan layanan yang terus-menerus, seperti server web atau database, yang siap menerima permintaan kapan saja tanpa perlu intervensi manual.
4. Pengelolaan Jaringan:
   Daemon sering digunakan untuk mengelola layanan jaringan, seperti DNS, DHCP, dan server email, yang penting untuk operasi jaringan yang efisien.
5. Keamanan:
   Beberapa daemon, seperti 'sshd', menyediakan lapisan keamanan tambahan dengan mengelola akses ke sistem melalui protokol yang aman.

