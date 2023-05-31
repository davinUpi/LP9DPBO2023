# LP9DPBO2023

### Saya Davin mengerjakan evaluasi LATIHAN9DPBO2023 dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Penjelasan kelas
![class diagram drawio](https://github.com/davinUpi/LP9DPBO2023/assets/100902319/ae07dcda-3794-497a-883f-e6fa59d9b350)

### kelas objects
Semua kelas pada folder objects memiliki fungsionalitas yang sama: merepresentasikan value/ row sebuah tabel. Tabel yang dimaksud
sesuai dengan nama objectnya. Kelas2 object merupakan hasil return dari setiap models

### Abstract Kelas Database
Kelas ini merupakan konfigurasi untuk terkoneksi dengan basis data MySQL. Adapun konfigurasi
sudah secara default menggunakan konfigurasi yang tertera di dalam Cofig.py. Selain itu, digunakan
juga untuk mengeksekusi query. Merupakan abstract class sehingga tidak bisa dinstansiasi secara langsung

### Kelas Model(nama_tabel)
Karena banyak dan secara fungsionalitas sama, kelas-kelas yang memodelkan tabel2 yang digunakan.
Merupakan kelas turunan Database yang memiliki metode untuk mengambil semua atau mengambil satu berdasarkan
id. Adapun pengecualian adalah ModelFigure.py

### Kelas ModelFigure
Awalnya dirancang untuk melakukan CRUD pada tabel figure. Menggunakan ModelFigureType, ModelFigureManufacturer, dan ModelFigureSeries(seharusnya)
sebab mereferensi ketiga tabel tersebut dalam bentuk foreign key.

### Kelas App
merupakan kelas utama untuk menampilkan python gui. Terdiri dari dua metode utama: show_landingPage dan show_tablePage. show_landingPage
menampilkan landing page yang terdiri dari image dan button dimana bila di klik akan menjalankan show_tablePage. Secara default,
show_landingPage dijalankan ketika program pertama kali dijalankan.

show_tablePage merupakan metode untuk menampilkan page tabel2 dan menghancurkan page sebelumnya. metode ini memiliki navbar
yang terdiri dari button2 yang akan menjalankan metode2 tertentu untuk menampilkan tabel2 yang berbeda. Semua tabel sama
kecuali tabel figure. Value dari tabel figure dapat diklik untuk menampilkan pop-up detail dari figure tersebut, termasuk gambarnya

## demo
teralu badag, buka folder dokumentasi di asset
