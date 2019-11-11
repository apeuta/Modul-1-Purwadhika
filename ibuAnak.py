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
print (f"Jika umur Anak adalah {umurAnak} tahun, dan umur Ibu adalah {umurIbu} tahun, \nmaka umur ibu saat melahirkan adalah {umurLahiran} tahun")