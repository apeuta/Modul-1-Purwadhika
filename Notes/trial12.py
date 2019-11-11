'''
REVIEW
'''
# class X:
#     def __init__ (self, name, age):
#         self.nama = name
#         self.usia = age
#     def pensiun (self):
#         return (f"{self.nama} akan masuk pensiun dalam {55 - self.usia} tahun lagi")

# objX = X("Andi", 20)

# print (objX.nama)
# print (objX.usia)
# print (objX.pensiun())

'''
Fibbonaci
1,1,2,3,5,8...
'''
class fibo():
    def __init__(self,indeks):
        self.indeks = indeks
    def fibolist(self):
        deret = [0,1]
        for i in range (2, self.indeks +1):
            deret.append(deret[i-2] + deret [i-1])
        print (deret[1:])
        return deret[self.indeks]
inputan = int(input("Deret fibbonaci keberapa yang ingin anda ketahui angkanya : "))
fibo = fibo(inputan)
print (f"Deret fibbonaci ke-{inputan} adalah {fibo.fibolist()}")
'''
Ubah Karakter
aBcDEFghi -> AbCdefGHI
'''
# def uplow(x):
#     y = list(x)
#     z = []
#     for i in y:
#         if i == i.upper():
#             z.append(i.lower())
#         else:
#             z.append(i.upper())
#     print ("".join(z))
# kata = input("Masukkan kata dengan gabungan uppercase dan lowercase : ")
# uplow(kata)
'''
Cek sudut antara dua sisi segitiga
A = 8 cm    B = 10 cm, sudut AB = ?
'''

'''
[                                   [
    [1,2,3],                            [7,4,1],
    [4,5,6],            def =>          [8,5,2],
    [7,8,9]                             [9,6,3]
]                                   ]
'''
# numList = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# #clockwise
# cw = [[numList[j][i] for j in range(len(numList))] for i in range (len(numList[0]))]
# #counterclockwise
# ccw = [[numList[j][i] for j in range(len(numList))] for i in range (len(numList[0])-1,-1,-1)]
# print (cw)
# print (ccw)