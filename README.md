# Menghitung-Luas-dan-Keliling-Lingkaran
## Rumus Luas dan Keliling Lingkaran

```bash
Luas     = π × r²
Keliling = 2 x π × r
```

![IMG 1](screenshoot/ss1.jpg)

- Nilai phi yang di gunakan adalah 3.14
- r merupakan jari-jari lingkaran

Phi merupakan nilai konstanta di matematika sementara jari-jari merupakan jarak antara titik pusat dengan tepi lingkaran. Sebetulnya ada rumus lain untuk menghitung keliling lingkaran yaitu dengan menggunakan diameter, tapi pada kasus ini kita cukup menggunakan jari jari lingkaran saja.

### Flowchart Menghitung Luas dan Keliling Lingkaran

![IMG 2](screenshoot/ss2.png)

### Program Menghitung Luas dan Keliling Lingkaran

```bash
phi = 3.14
// Input
r = float(input("Masukan jari-jari lingkaran : "))
// Rumus
luas = phi*(r*r)
keliling = 2*phi*r
// Output
print ()
print ("Rumus Luas Lingkarannya \t=",phi,"x",r,"x",r,)
print ("Rumus Keliling Lingkaran \t=",2,"x",phi,"x",r,)
print ()
print ("Hasil Luas Lingkaran \t\t= ",format(luas,'.2f'))
print ("Hasil Keliling Lingkaran\t= ",format(keliling,'.2f')
```

### Penjelasan

Selanjutnya kita memerlukan nilai jari-jari (r) yang nantinya akan di masukan oleh pengguna pada layar console. Kita menggunakan fungsi input() yang nilainya di konversi ke tipe data float (bilangan riil). Ingat bahwa fungsi input() akan menganggap semua nilai inputan bertipe string, sehingga kita perlu melakukan konversi ke tipe yang diinginkan.

Ketika kita sudah mendapat nilai phi dan jari-jari selanjutnya kita bisa menghitung luas dan keliling sesuai dengan rumus-nya.

Selanjutnya kita tampilkan hasilnya dengan fungsi print(). sintak \t merupakan karakter espace yang berfungsi untuk membuat tab. dalam kasus ini agar sejajar karakter sama dengan (=) nya.

Jika dilihat hasil luas dan keliling lingkaran mempunyai angka pecahan yang cukup banyak, untuk mengambil 2 angka pecahan saja kita pakai fungsi format() seperti gambar di atas.

### Output

[IMG 3](screenshoot/ss3.png)

### TERIMA KASIH