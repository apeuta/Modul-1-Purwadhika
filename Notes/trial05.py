'''
angka = int(input ("Masukkan angka : "))
if (angka % 2) == 0:
    print (f"{angka} adalah bilangan Genap")
else:
    print (f"{angka} adalah bilangan Ganjil")
'''
'''
angka = 1
while (angka <= 10):
    print (angka)
    angka += 1
'''
'''
# listItem = list(range(1,11,2))
# print (listItem)

for item in range (1,11,1):
    print (f"Nomor urut {item}")
'''
'''
z = ""
for item in range (0,5):
     for item1 in range (0, item + 1):
         z += "* "
     z += "\n"
print (z)
'''
'''
#function
def hello():
    print ("Hello World!")
#hello ()

#f(x) = x ^ 3
def pangkat3 (anu):
    print (anu ** 3)

# pangkat3 (2)
# pangkat3 (3)

def pangkat (a1, a2):
    print (a1 ** a2)
pangkat (float(input("Ketik angka 1 : ")), float(input("Ketik angka 2 : ")))
'''
'''
def gangen(x):
    if (x % 2) == 0:
        print (f"{x} adalah bilangan Genap")
    else:
        print (f"{x} adalah bilangan Ganjil")

gangen (int(input("Masukkan angka : ")))
'''
'''
#function basic calculator

def kalk():
    a = float(input("Masukkan angka 1 : "))
    x1 = (input("Masukkan operator aritmatika (+-*/) : "))
    b = float(input("Masukkan angka 2 : "))
    if x1 == "+":
        print (a + b)
    elif x1 == "-":
        print (a - b)
    elif x1 == "*":
        print (a * b)
    elif x1 == "/":
        print (a / b)
    else:
        print ("Maaf operator tidak dikenali")

kalk()
'''
'''
# Function bisa panggil variabel dari luar
# Tapi variabel di dalam function tidak bisa dipanggil keluar

students = ["Andi", "Budi", "Caca"]
teachers = ["Newton", "Einstein", "Curie"]
def tes (x):
    print (x[0])
    print ("Caca" in x)

tes(students)
tes(teachers)

#return function
Return Function bisa diprint bila mereturn fungsi tertentu
def returnHello():
    return "Helo Wooooorld!!"

print returnHello()
'''
'''
def vocal(kata):
    kata = kata.replace("a","o")
    kata = kata.replace("i","o")
    kata = kata.replace("u","o")
    kata = kata.replace("e","o")
    print (kata)

vocal(input("Masukkan kata : "))
'''
# i = 20
# while i >= 1:
#     print (i)
#     i -= 1

# students = ["Andi", "Budi", "Caca", "Deni"]
# index = 0
# while index <= len (students) -1:
#     print(students[index])
#     index += 1

# x = [1,2,3,4,5,6,7,8,9,10]
# y = []
# index = 0
# while index <= len(x)-1:
#     y.append(x[index]**2)
#     index += 1

# print (y)

# i = 1
# while i < 10:
#     print (i)
#     if i == 5:
#         break
#     i +=1

# i = 0
# while i < 10:
#     i+= 1
#     if i == 5:
#         continue
#     print(i)

password = "aiueo"
# status = False
# if input("Masukkan password : ") != password:
#     while status == False:
#         userInput = input("Password salah! Masukkan lagi : ")
#         if userInput == password:
#             status = True
#             print ("Password Benar!")
#         else:
#             userInput
# else:
#     print ("Password Benar!")
inputan = ""
coba = 0
batas = 3
lebih = False
# while inputan != password:
#     inputan = input("Ketik password : ")
#     coba += 1
#     if inputan != password:
#         print ("Password Salah!")
#         if coba == batas:
#             print ("KESEMPATAN HABIS COBA 5 MENIT LAGI!")
#             break
#     else:
#         print("Password Benar!")

while inputan != password and not lebih:
    if coba < batas:
        inputan = input(
            f"Input ke-{coba + 1} ketik password : "
        )
        coba += 1
    else:
        lebih = True

if lebih:
    print("Kesempatan habis! Coba 5 menit lagi...")
else:
    print("Password benar!")