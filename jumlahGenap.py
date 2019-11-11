'''
Contoh soal
angka 1-100
diambil genap -> dikali 2 -> lalu dijumlahkan semua
'''
nomor = list (range (1,101))
from functools import reduce
jumGen = reduce(lambda x, y : x + y, map(lambda x : x * 2, filter(lambda x : x % 2 == 0, nomor)))
print (jumGen)