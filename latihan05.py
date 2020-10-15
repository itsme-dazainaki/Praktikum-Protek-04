laki = int(input("Banyak siswa Laki-Laki = "))
prpn = int(input("Banyak siswa Perempuan = "))

diagram1 = laki//10
diagram2 = prpn//10

print("Berikut adalah Diagram horizontalnya :")
print(diagram1*"*",laki)
print(diagram2*"*",prpn)