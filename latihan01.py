#mari menginput
pinjam1 = int(input("Jam pinjam = "))
pinjam2 = int(input("Menit pinjam = "))
kembali1 = int(input("Jam kembali = "))
kembali2 = int(input("Menit kembali = ")) 
#variabel juga nih
awal = 200000
lanjut = 10000
menit = 10000/60
#ini rumusnya
print("Tarif sewa anda : ", awal +(((kembali1-pinjam1)-12)*lanjut))
