'''
Lambda Function
'''
# x = lambda a, b, c : a * b + c
# #sama dengan
# def y(a, b, c):
#     return a * b + c

# print (x(4,5,6))
# print (y(4,5,6))

'''
Fungsi turunan dengan menggunakan lambda
'''
# def myFunction (x):
#     return lambda a : a ** x

# pangkat2 = myFunction(2)
# pangkat3 = myFunction(3)
# pangkat4 = myFunction(4)

# print (pangkat2(9))
# print (pangkat3(5))
# print (pangkat4(2))

'''
Map Python
'''
# #Contoh 1
# def y(a):
#     return len(a)
# a = ["Andra", "Pranata", "Utama"]
# x = map(y, a)
# print (list(x))

# #Contoh 2
# topping = ["Coklat", "Keju", "Boba"]
# rasa = ["Teh", "Kopi", "Susu"]
# def combi (a,b):
#     return a + " " + b
# bla = map (combi, rasa, topping)
# print (list(bla))

# #Contoh 3
# x = [2, 4, 6, 8, 10]
# #Cara 1
# def y (a):
#     return a**2
# z = map(y, x)
# print (list(z))
# #atau
# #Cara 2
# anu = map (lambda a: a**2, x)
# print (list(anu))
# #atau
# #Cara 3
# b = []
# for i in x:
#     b.append(i ** 2)
# print (b)

'''
Fungsi Filter
'''
# x = range (11)
# #Cara 1
# def kurangLima(x):
#     if x < 5:
#         return False
#     else:
#         return True

# y = filter (kurangLima, x)
# print (list(y))

# #Cara 2
# z = filter (lambda a: True if a >= 5 else False, x)
# print (list (z))

# #Fungsi pangkat
# x = pow (2, 2)
# y = pow (3, 3)
# print (x)
# print (y)

# z = list (map(pow, [2,3], [2,3]))
# print (z)

# #melihat elemen yang ada di 2 list
# x = [1, 3, 5, 7, 9]
# y = [3, 6, 9, 12, 15]
# z = list(filter(lambda a: a in x, y))
# print (z)

'''
Fungsi Reduce
'''
# angka = [1,2,3,4]
# hasil = 1
# for i in angka:
#     hasil *= i
# print (hasil)

# from functools import reduce
# z = reduce (lambda x, y : x * y, angka)
# print (z)

# kata = ["Ini", "Ibu", "Budi"]
# print (" ".join(kata))

# import functools
# z = functools.reduce (lambda x, y : x + " " + y, kata)
# print (z)

'''
Filter in Map
'''
# angka = [1, 2, 3, 4]
# #output list dari angka x 2 yang lebih dari 3
# z = list (filter(lambda x : x > 3, map(lambda x : x * 2, angka)))
# print (z)
# #output list dari angka lebih dari 3 dikalikan 2
# y = list (map(lambda x : x * 2, filter(lambda x : x > 3, angka)))
# print (y)

'''
Contoh soal
angka 1-100
diambil genap - dikali 2 - lalu dijumlahkan semua
'''
nomor = list (range (1,101))
from functools import reduce
# mancing = reduce(lambda x, y : x + y, map(lambda x : x * 2, filter(lambda x : x % 2 == 0, nomor)))
# print (mancing)

#bilangan prima
prima = list(filter(lambda x : x % 7 or x == 7, 
filter (lambda x: x % 5 or x == 5, 
filter(lambda x: x % 3 or x == 3, 
filter(lambda x: x % 2 or x == 2, 
filter (lambda x : x>1, nomor))))))

print (prima)
print (len(prima))

prime = list(filter (lambda x :(x % 7  or x == 7) and (x % 5  or x == 5) and 
(x % 3  or x==3) and (x % 2  or x == 2) and (x > 1) , nomor))
print (prime)

def primus (x):
    a = False
    if x > 1:
        if x == 2: a = True
        else:
            for i in range (2, x):
                if x % i == 0: a = False; break
                else: a = True
    else: a = False
    return a

z = list (filter(primus, range(101)))
print (z)