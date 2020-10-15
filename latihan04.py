#ini untuk menginput jarak yang ditempuh
jarak1 = int(input("Jarak pertama  = ")) 
jarak2 = int(input("Jarak kedua = "))
print("------------------")
kec1 = int(input("Kecepatan pertama = ")) 
kec2 = int(input("Kecepatan kedua  = "))
print("------------------")
mangkat1 = int(input("Jam saat berangkat = ")) 
mangkat2 = int(input("Menit saat berangkat = "))
print("------------------")
ist1 = int(input("Waktu istirahat dalam jam = ")) 
ist2 = int(input("Waktu istirahat dalam menit = ")) 

#menghitung waktu yang ditempuh
waktu1 = round(jarak1/kec1)
waktu2 = round(jarak2/kec2)

#ini buat menghitung waktu sampai
print("------------------")
print("Pak Amir akan sampai pada pukul =", (mangkat2 + mangkat1 + ist1 + ist2/100 + waktu1 + waktu2))