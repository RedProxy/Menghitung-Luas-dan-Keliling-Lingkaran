print("Program Menghitung Luas dan Keliling Lingkaran")
print("==============================================")
r = float(input("Masukan Jari-Jari Lingkaran  : "))

phi = 3.14
luas = phi*r*r
kel = 2*phi*r

print ()
print ("Rumus Luas Lingkarannya \t=",phi,"x",r,"x",r,)
print ("Rumus Keliling Lingkaran \t=",2,"x",phi,"x",r,)
print ()
print ("Hasil Luas Lingkaran :",format(luas,'.2f'))
print ("Hasil Keliling Lingkaran :",format(kel,'.2f'))
