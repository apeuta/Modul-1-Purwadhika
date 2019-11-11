'''
#SOAL 1
19 tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibu
umur anak sekarang 19 tahun lebih tua dari sepertujuh umur ibu
umur ibu?

Trial rumus
6 tahun lalu, umur anak setengah tahun lebih muda dari seperempat umur ibu
umur anak sekarang lebih tua 9 tahun dari seperdelapan umur ibu
'''
rasioDulu = (1/4)
selisihDulu = 19
selisihUmur = 0.5
rasioKini = (1/7)
selisihKini = 19
rasio = (rasioKini / rasioDulu)
rasioBanding = ((1/rasioKini) - (1/rasioDulu))

umurAnak = (selisihKini + (rasio * (selisihUmur - selisihDulu + (selisihDulu * rasioDulu)))) / (rasioBanding * rasioKini)
umurIbu = ((1/rasioKini) * (umurAnak - selisihKini))
umurLahiran = umurIbu - umurAnak
print (f"Jika umur Anak adalah {umurAnak} tahun, dan umur Ibu adalah {umurIbu} tahun, maka umur ibu saat melahirkan adalah {umurLahiran} tahun")
# print (rasioDulu)
# print (rasioKini)
# print (selisihDulu - selisihUmur)
'''
Umur andi dan umur ayahnya sekarang jumlahnya 50 tahun.empat tahun yang lalu umur ayah andi 6 kali umur andi.umur andi dan umur ayahnya saat ini adalah??
'''
# rasioKini = 1
# lamaLampau = 4
# rasioLampau = 6
# jmlUsia = 50
# usiaAyah = (((rasioLampau) * (jmlUsia - lamaLampau)) + lamaLampau) / ((1/rasioKini)+rasioLampau)
# usiaAndi = jmlUsia - usiaAyah
# print (f"Umur Andi saat ini adalah {usiaAndi} tahun, dan umur ayah adalah {usiaAyah} tahun")