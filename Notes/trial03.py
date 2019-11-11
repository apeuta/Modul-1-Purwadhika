'''
Edit Tuple and List
'''
# x = [
#     (1, ["a", "b","c"],3),
#     (4,5,6)
# ]
# x[0][1][2] = "Andi"
# x [0][1].append("d")

# print (x)
# x = [1 , 2, 3 , 1 , 2 , 3]
# y = (1 , 2 , 3)
# # set / himpunan
# # no indexing  
# # duplicate elements are not allowed 
# # element must be immutable
# z = {1 , 2 , 3 , 1 , 2 , 3}
# #print (list(set(x)))
# '''
# masukkan 1 elemen pakai add
# masukkan beberapa elemen pakai update
# '''
# z.add ("a")
# z.add (("c" , "d" , "e"))
# z.update ("andi")
# z.update ({"z", "budi"})
# #update dengan string atau mutable akan tersplit
# z.update("andi")
# print (z)
# '''
# remove >> perintah untuk hapus data yg ada
# discard >> perintah untuk hapus data, tidak error walau data tidak ada
# '''
# z.remove("budi")
# z.discard("deni")
# print(z)
# z.pop ()
# z.pop ()
# print (z)
# del (z)
# print (z)

'''
Irisan
'''
a = list ("abcde")
b = list ("bcfgh")
#A irisan B = {b,c}
a = set (a)
b = set (b)
# print (a.intersection(b))
# print (a & b)

# #A gabungan B
# print (a.union(b))
# print (a | b)

# # selisih / difference
# print(a.difference(b))
# print(b.difference(a))
# print (a - b)
# print (b - a)

#symmetric diff
# print (a.symmetric_difference(b))
# print (a ^ b)

# P  = set([1,2,4,7,9,19])
# Q = set([5,7,9,19,6,12,16,17])
# R = set([3,6,8,19])
# print (P & Q)
# print (P & Q & R)
# print (P ^ Q ^ R)

# P = []
# Q = []
# R = []
# S = []

# for i in range (-9,10,1):
#     S.append(i)
# for i in range (-4,5,1):
#     P.append(i)
# for i in range (-7,2,1):
#     Q.append(i)
# for i in range (-1,8,1):
#     R.append(i)
# P = set(P)
# Q = set(Q)
# R = set(R)
# S = set(S)
# print (P)
# print (Q)
# print (R)
# print (S)
# BB = (P | Q | R | S)
# BB = list(BB)
# print (BB)
# BB.sort()
# print (BB)
# nilai = int(input ("Masukkan nilai... "))
# if (nilai > 80):
#     print ("Mangstab!")
# elif (nilai >= 60 and nilai <=80 ):
#     print ("Mayaaan")
# else:
#     print ("Semangat cuy")
# massa = int(input("Masukkan massa (kg) : "))
# tinggi = int(input ("Masukkan tinggi (cm) : "))
# Indeks = massa / (tinggi/100) ** 2
# print (f"Jika berat anda {massa} kg dan tinggi anda {tinggi} cm, maka ...")
# if (Indeks < 18.5):
#     print ("Berat badan kurang")
# elif (Indeks >= 18.5 and Indeks< 25):
#     print ("Berat badan ideal")
# elif (Indeks >= 25 and Indeks<30):
#     print ("Berat badan berlebih")
# else:
#     print ("Berat badan sangat berlebih")

angka = 1
while (angka<=10):
    print (angka)
    angka+=1