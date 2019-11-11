# angka = 5
# # angka1 = 2
# while angka > 0:
#     print (angka * "*")
#     angka -= 1
# while angka1 <=5:
#     print (angka1 * "*")
#     angka1 += 1
# def welcome (a_string):
#     print ("Welcome", a_string, "!" )

# a_string = input("Siapa Namamu?")
# welcome (a_string)

# jowo = {"satu" : "siji", "dua" : "loro"}

# jowo.update({"tiga": "telu"})
# print (jowo)

#piramida
# cap = 1
# for bil in range (1,20,2):
#     print ((20 - cap)* " " + bil * "* ")
#     cap += 2

#piramida
# cap = 1
# for bil in range (1,20,2):
#     print (cap * " " + (20 - bil)* "* " + bil * " ")
#     cap += 2

# buah = [1,5,12,3,5,6]
# buah.sort()
# print (buah[(len(buah)-1)])

'''
kota = ["Jakarta", "Bandung", "Surabaya"]
i = 0
#cara 1
while i < len(kota):
    print (kota[i])
    i += 1

#cara 2
for i in range(len(kota)):
    print (kota[i])

#cara 3
for namaKota in kota:
    print (namaKota)

'''
# for i in range (1,11):
#     if (i % 2) != 0:
#         print (i)
#     else:
#         print ("Wow!")
'''
def fizzbuzz(x):
    for i in range (1,x+1):
        if (i % 3) == 0 and (i%5 == 0):
            print ("FizzBuzz")
        elif (i % 5) == 0:
            print ("Buzz")
        elif (i % 3) == 0:
            print ("Fizz")
        else:
            print (i)

fizzbuzz (15)
'''
'''
Cara membalik urutan list
x = [1, 2, 3, 4, 5]

#cara 1
x.reverse()
print (x)

#cara 2
print (x[::-1])

#cara 3
print (list(reversed()))
'''
# y = ["Andi", "Budi", "Caca"]
# def walikan(x):
#     print (list(reversed(x)))

# walikan(y)

# y.sort(reverse=True)
# print (y)
'''
#Ganti o tanpa replace
hurufvokal = list ("aiueo")
def gantio(x):
    newString = ""
    for i in x.lower():
        if i in hurufvokal:
            newString += "o"
        else:
            newString += i
    print (newString) 

gantio(input("Masukkan kata : "))
'''

'''
#Temporary Method
anu = [1, 2, 4, 6, 8, 9]

def walik(vari):
    temp = 0
    final = len(vari)-1
    if len(vari)%2 == 1:
        for i in range (0, int(len(vari)/2)+1):
            temp = vari[i]
            vari[i]= vari[final]
            vari[final] = temp
            final -= 1
        print (vari)
    else:
        for i in range (0, int(len(vari)/2)):
            temp = vari[i]
            vari[i] = vari[final]
            vari[final] = temp
            final -= 1
        print (vari)

walik(anu)
'''
'''
x = [1, 3, 5, 7, 9, 11]
y = ["Andi", "Budi", "Caca"]

def balikPosisi(sesuatu):
    hasil = []
    for i in range (len(sesuatu)):
        hasil.insert(0, sesuatu[i])
    return hasil

print (balikPosisi(x))
print (balikPosisi(y))
'''
# bla = input("Masukkan kata : ")
# def palin (kata):
#     if kata[::-1] == kata:
#         print (True)
#     else:
#         print (False)

# palin(bla)

# #list to string
# hmm = "keramat"
# y = list(hmm[::-1])
# y = "".join(y)
# print (y)
