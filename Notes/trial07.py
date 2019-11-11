# # # morse program
# # morse = {"a":".- ", "b" : "-... ", "c":"-.-. ","d":"-.. ","e":". ","f":"..-. ","g":"--. ","h":".... ",
# # "i":".. ", "j":".--- ","k":"-.- ","l":".-.. ","m":"-- ","n":"-. ","o":"--- ","p":".--. ","q":"--.- ",
# # "r":".-. ","s":"... ","t":"- ","u":"..- ","v":"...- ","w":".-- ","x":"-..- ","y":"-.-- ",
# # "z":"--.. ", " ":"/"}
# # mor = list(morse)
# # rse = list(morse.values())
# # def conmors(x):
# #     newString = ""
# #     for i in x.lower():
# #         if i in mor:
# #             newString += (morse.get(i))
# #         else:
# #             vari = mor[rse.index(i)]
# #             newString += (vari)
# #     print (newString)

# # conmors(input("Masukkan morse/kata yang ingin diubah : \n"))

# # angka = 5
# # angka1 = 2
# # while angka > 0:
# #     print (angka * "*")
# #     angka -= 1
# # while angka1 <=5:
# #     print (angka1 * "*")
# #     angka1 += 1

'''
Piramida ok
1
22
333
'''
# # def pira (x, y):
# #     for x in range (x,y+1):
# #         print (x * str(x))
# # pira(1,5)

'''
Piramida ok
1
12
123
'''
# def some (v, w):
#     anu = ""
#     for v in range (v,w+1):
#         anu += str(v)
#         print (anu)
# some (1,5)

'''
Piramida ok
123
12
1
'''
# def bla (x):
#     for row in range (x,0,-1):
#         for col in range (1,row+1):
#             print (col,end=" ")
#         print()
# bla (5)

'''
Piramida ok
321
32
3
'''
# def bla (x):
#     for row in range (1,x+1,1):
#         for col in range (x,row-1,-1):
#             print (col,end=" ")
#         print()
# bla (5)
'''
Piramida ok
3
32
321
'''
# def bla (x):
#     for row in range (x,0,-1):
#         for col in range (x,row-1,-1):
#             print (col,end=" ")
#         print()
# bla (5)

# #pangkat tanpa ** dan pow
# def pangkat (x,y):
#     out = 1
#     for i in range(y):
#         out *= x
#     print(out)
# pangkat (2,3)

# def pangkatB (v,w):
#     if (w == 1):
#         return v
#     else:
#         return v * pangkatB(v, w-1)
# print(pangkatB(3,3))

# #faktorial tanpa math
# import math
# print (math.factorial(0))

# def faktor (n):
#     out = 1
#     for i in range(n):
#         out *= n
#         n-=1
#     print(out)
# faktor (0)


#piramida
cap = 1
for bil in range (1,20,2):
    print (cap * " " + (20 - bil)* "* " + bil * " ")
    cap += 2


#piramida
cap = 1
for bil in range (1,20,2):
    print ((20 - cap)* " " + bil * "* ")
    cap += 2