# TugasBesarMBD

Tugas Besar ini adalah pembuatan interface (GUI) pada database yang telah digunakan pada tugas sebelumnya (juga merupakan pengembangan dari tugas mata kuliah Basis Data semester 3). 

# Penggunaan Bahasa Pemrograman Python 
Dalam tugas ini, bahasa pemrograman yang digunakan adalah bahasa pemrograman python. Hal ini dikarenakan bahasa pemrograman ini dianggap lebih sederhana dan mudah untuk dipahami, selain itu banyaknya resources yang tersedia membuat pengembangan sistem akan lebih mudah untuk dilakukan.

![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Tkinter.png)

Dalam pengembangan sistem ini, untuk mendukung pembuatan Graphic User Interface (GUI) library yang digunakan pada python adalah library Tkinter yang memang ditujukan untuk penggunaan pembuatan Graphic User Interface. Tkinter memiliki banyak package yang dapat digunakan seperti messageboxm, frame, button dan lain sebagainya yang akan mendukung pengembangan program. 

# Database 
Database yang digunakan terdiri dari 6 tabel yaitu distributor, komputer, pegawai, pembayaran, pembeli, dan pesanan. Database ini merupakan manajemen suatu toko komputer yang perlu untuk diimplementasikan dalam bentuk interface sebagai kualifikasi dari tugas besar dari mata kuliah manajemen basis data. Dilakukan pengujian dalam data-data yang telah dibuat dengan interface yang dikembangkan yang masing-masing dihubungkan dengan database. 

# Interface Aplikasi 
Pengembangan interface aplikasi yang adalah untuk aplikasi desktop, interface yang digunakan adalah menggunakan interface yang memiliki fungsi untuk add data, display, update, delete, search, reset, dan exit. Awalnya fungsi yang ingin digunakan hanya untuk melakukan search pada database, tetapi setelah pengembangan dan diskusi lebih lanjut akhirnya dibuatkan fungsi yang lebih kompleks yaitu sesuai dengan yang telah sebelumnya dipaprkan. Berikut adalah gambar prototype dari aplikasi yang dikembangkan. 
![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Protoype.png)
<br><br/>
Pada saat pengembangan selanjutnya untuk menghubungkan database library yang digunakan adalah library pymysql yang cukup mudah untuk dipahami. Dengan library ini database dan GUI dapat disambungkan, implementasinya dapat ditunjukkan dari kode berikut.

![alt text](pymysql)

Untuk source code yang digunakan dilampirkan pada pemrograman berikut adalah interface dari masing-masing tampilan implementasi GUI : 

<br>Distributor:<br/>

![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Interface_Distributor.png)

<br>Komputer:<br/>

![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Interface_Pegawai.png)

<br>Pegawai:<br/>
![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Interface_Pegawai.png).

<br>Pembayaran :<br/>
![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Interface_Pembayaran.png)

<br>Pembeli :<br/>
![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Interface_Pembeli.png)

<br>Pesanan :<br/>
![alt text](https://github.com/gerynsb/TugasBesarMBD/blob/main/Img/Interface_Pesanan.png)



