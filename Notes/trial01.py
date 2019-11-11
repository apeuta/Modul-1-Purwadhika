# x = input("Berapa nilai x? ")
# y = input("Berapa nilai y? ")
# z = input("Berapa nilai z? ")
# print " "
# print "Jika w adalah ((x + y * z)/(x * y))^z"
# print "maka w"
# a = x + y * z
# b = x * y
# c = float(a) / b
# print c ** z


#485 hari
'''
hari1 = 750
tahun = round(hari1/365)
bulan1 = (hari1 % 365)
bulan = round(bulan1 / 30)
hari = (bulan1 % 30)
print (f"{hari1} hari adalah {tahun} tahun, {bulan} bulan, dan {hari} hari")
'''

'''
#Usia Andi + Budi = 49
#Usia Andi : Budi = 4 : 10
jumlahUsia = 49
Rasio = 0.4
Andi = ((Rasio) / (Rasio + 1)) * jumlahUsia

import math

hari1 = (Andi * 365)
tahunA = round(hari1/365)
bulan1 = (hari1 % 365)

bulanA = math.floor(bulan1 / 30)
hariA = math.ceil(bulan1 % 30)

hari2 = (jumlahUsia * 365) - (Andi * 365)
tahunB = round(hari2/365)
bulan2 = (hari2 % 365)

bulanB = math.floor(bulan2 / 30)
hariB = math.ceil(bulan2 % 30)
print (f"Usia Andi adalah {tahunA} tahun, {bulanA} bulan, {hariA} hari dan usia Budi adalah {tahunB} tahun, {bulanB} bulan, {hariB} hari ")
'''
'''
#Program cari huruf
teks = "Salam hangat terdahsyat untuk seluruh keluarga Indonesia"
cariHuruf = input("Masukkan huruf yang ingin anda cari? ")
abc = teks.lower().replace(cariHuruf,"")
jmlCari = len(teks) - len(abc)
print (f"Jumlah huruf {cariHuruf} yang anda cari adalah ...")
print (jmlCari)
'''

#Program cari pertemuan

# Jarak A dan B = 120
# Kecepatan A = 60
# Kecepatan B = 40
# Berangkat jam 9,ketemu kapan?

Distance = 120
speedA = 60
speedB = 40
menit = int((Distance / (speedA + speedB))*60)
import math
jam = math.floor(menit / 60)
menit1 = int(menit % 60)
print (f"{menit} menit setelah jam 09.00")
print (f"{jam} jam dan {menit1} menit ")
