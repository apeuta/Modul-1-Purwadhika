'''
REVIEW SESSION
'''
# #inheritance
# class Manusia:
#     def __init__ (self, nama):
#         self.nama = nama

# class Pria:
#     def __init__ (self, nama):
#         Manusia.__init__(self, nama)
#         self.gender = "Laki-laki"

# class Wanita:
#     def __init__ (self, nama):
#         Manusia.__init__(self, nama)
#         self.gender = "Perempuan"

# objA = Manusia("Andi")
# objB = Pria("Andi")
# objC = Wanita ("Andi")

# print (vars(objA))
# print (vars(objB))
# print (vars(objC))

# #Multi Level Inheritance
# class X:
#     def __init__(self, x):
#         self.x = x

# class Y(X):
#     def __init__(self, x, y):
#         X.__init__(self, x)
#         self.y = y

# class Z(Y):
#     def __init__(self, x, y, z):
#         Y.__init__(self, x, y)
#         self.z = z

# objA = Z ("Andra", "The", "Backbone")
# print (vars(objA))

# #Multiple Inheritance
# class Carnivore:
#     def __init__(self):
#         self.meats = True

# class Herbivore:
#     def __init__(self):
#         self.veggies = True

# class Omnivore(Carnivore, Herbivore):
#     def __init__(self):
#         Carnivore.__init__(self)
#         Herbivore.__init__(self)
#         self.McD = True

# ObjA = Omnivore()
# print (vars(ObjA))

'''
IMPORT
'''
# import trial9 as anu
# print (anu.halo("Andra"))
# print (anu.PersegiA)

import datetime as hmm
x = hmm.datetime.now()
# print (x)
# print (x.strftime("%d")) #date
# print (x.strftime("%A")) #day
# print (x.strftime("%m")) #month number
# print (x.strftime("%B")) #month
# print (x.strftime("%Y")) #year
# print (x.strftime("%H")) #hour 24h
# print (x.strftime("%I")) #hour 12h
# print (x.strftime("%p")) #am/pm
# print (x.strftime("%M")) #min
# print (x.strftime("%S")) #sec
# print (x.strftime("%c")) #info waktu lengkap
# print (x.strftime("%x")) #tanggal lengkap
# print (x.strftime("%X")) #jam lengkap

hariIndo = {
    "Monday": "Senin", "Tuesday":"Selasa" , "Wednesday": "Rabu",
    "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
}
bulanIndo = {
    "January": "Januari", "February":"Februari" , "March": "Maret",
    "April": "April", "May": "Mei", "June": "Juni", "July": "Juli",
    "August":"Agustus", "September":"September", "October":"Oktober",
    "November":"Nopember","December":"Desember"
}

class time:
    def __init__ (self):
        self.hari = (hariIndo.get(x.strftime("%A")))
        self.tanggal = x.strftime("%x")
        self.bulan = bulanIndo.get(x.strftime("%B"))
        self.tahun = x.strftime("%Y")
        self.jam = x.strftime("%H")
        self.menit = x.strftime("%M")
        self.detik = x.strftime("%S")

waktu = time()

angka1 = [1, 2, 9, 4, 5, 6, 7, 8, 3, 3]
angka2 = [1, 2, 10, 4, 5, 3, 7, 8, 9, 6, 6]

class Statistika:
    def rerata (self, x):
        y = sum(x) / len (x)
        return y
    def nilaiTengah (self, x):
        x.sort()
        if len(x)%2 == 0:
            y = (((x[int((len(x))/2)]) + (x[(int((len(x))/2))-1]))/2)
        else:
            y = (x[int((len(x))/2)])
        return y
    def modus (self, x):
        default = 0
        angka = 0
        for y in x:
            if x.count(y) > default:
                default = x.count(y)
                angka = y
        return angka

stat = Statistika()