'''
Faktorial
'''
def faktor (n):
    out = 1
    for i in range(n):
        out *= n
        n-=1
    return out
angka = int(input("Masukkan angka faktorial : "))
print (f"Hasil dari {angka}! adalah {faktor (angka)}")

'''
Pangkat
'''
from functools import reduce
def Pangkat(x, y):
    hmm = []
    for i in range(y):
        hmm.append(x)
    hasil = reduce(lambda a,b: a*b, hmm)
    return hasil
x = int(input("Masukkan angka : "))
y = int(input("Masukkan pangkat : "))
print (f"Hasil dari {x}^{y} adalah {Pangkat (x, y)}")