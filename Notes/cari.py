# nama = "Hari ini Hari tidak masuk sekolah"
# cari = "h"
# x = nama.lower().replace(cari , "")
# print (x)
# jmlCari = len (nama) - len (x)
# print ("Jumlah huruf '{}' ada = {}".format(cari , jmlCari))

nama = "Hari ini Hari tidak masuk sekolah karena hari Minggu"
cari = "hari"
x = nama.lower().replace(cari , "")
print (x)
jmlCari = int((len(nama) - len (x)) / len (cari))
print ("Jumlah kata '{}' ada = {}".format(cari , jmlCari))