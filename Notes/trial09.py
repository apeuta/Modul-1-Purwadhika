'''
Class -> Cetakan object
'''
# #INTRO
# class Mobil:
#     warna = "Merah"
#     tahun = 2010

# #create object mobil1
# mobil1 = Mobil()
# print (mobil1)
# print (mobil1.warna)
# print (mobil1.tahun)

# #Beda input dalam 1 class
# class MobilCustom:
#     def __init__ (self, warna, tahun, model):
#         self.color = warna
#         self.year = tahun
#         self.model = model
#     #method
#     def jadul(self):
#         if self.year < 2010:
#             return True
#         else: return False
#     def tes (self):
#         print (self.color, self.year, self.jadul())

# mobil1 = MobilCustom ("Merah", 1998, "X")
# mobil2 = MobilCustom ("Biru", 2012, ["A", "B"])

# print (mobil1.color)
# print (mobil1.year)
# print (mobil1.model)
# print (mobil2.model)
# print (mobil1.jadul())
# print (mobil1.tes())

# #Inheritance Object
# class Car(MobilCustom):
#     pass
# #sama dengan
# class Car(MobilCustom):
#     def __init__(self, warna, tahun, model):
#         MobilCustom.__init__(self, warna, tahun, model)
# #sama dengan
# class Car(MobilCustom):
#     def __init__(self, warna, tahun, model):
#         MobilCustom.__init__(warna, tahun, model)

# class Supercar(MobilCustom):
#     gps = True

# car1 = Car ("Hijau", 2000, "M")
# supercar1 = Supercar ("Kuning", 2010, "F")
# print (car1.color, car1.year)
# print (supercar1.color, supercar1.year, supercar1.gps)

# #Menambahkan cetakan subclass/atribut
# class X:
#     def __init__ (self, nama):
#         self.nama = nama

# class Y(X):
#     def __init__ (self, nama, gelar):
#         super().__init__(nama)
#         self.gelar = gelar

# objX = X ("Andi")
# objY = Y ("Budi", "Dr.")

# print (objX.nama)
# #atau
# print (getattr(objX, "nama"))
# print (objY.gelar)
# print(vars(objY))
# from pprint import pprint
# pprint (vars(objY))

# #untuk cari tahu apakah ada atribut tertentu
# print (hasattr(objY, "nama"))
# print (hasattr(objY, "jalan"))

# #memodifikasi/menambahkan atribut

# objY.umur = 40
# #sama dengan
# setattr (objY, "umur", 40)
# print (vars(objY))
# delattr (objY, "umur")

# #Menghapus Atribut di dalam kelas
# class Z:
#     nama = "Andra"
#     asal = "Solo"

# objZ = Z()
# print (objZ.nama)
# print (objZ.asal)

# del Z.nama
# print (objZ.asal)

'''
Contoh
'''

# class student:
#     def __init__ (self, nama, usia):
#         self.nama = nama
#         self.usia = usia

# data = [
#     {"nama" : "Andi", "usia" : 21},
#     {"nama" : "Budi", "usia" : 22},
#     {"nama" : "Caca", "usia" : 23},
#     {"nama" : "Deni", "usia" : 24}
#     ]

# Andi = student (data[0].get("nama"),data[0].get("usia"))
# Budi = student (data[1].get("nama"),data[1].get("usia"))
# Caca = student (data[2].get("nama"),data[2].get("usia"))
# Deni = student (data[3].get("nama"),data[3].get("usia"))
# print (Andi.nama, Andi.usia)
# print (Budi.nama, Budi.usia)
# print (Caca.nama, Caca.usia)
# print (Deni.nama, Deni.usia)

# for i in data:
#     ehem = student(i["nama"], i["usia"])
#     print (f"Si {ehem.nama} berusia {ehem.usia}")

# dataNew = list (map (lambda x: student(x["nama"], x["usia"]), data))
# for i in range (len(dataNew)):
#     print (dataNew[i].nama, dataNew[i].usia)

# PERSEGI

class Persegi:
    def __init__ (self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2

PersegiA = Persegi(5)
print (vars(PersegiA))

def halo(a):
    return f"halo {a}"