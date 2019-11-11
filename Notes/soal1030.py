# Hai aku Lintang >> iaH uka gnatniL
print ("Program pembalik kata hirau spasi...")
word = input("Masukkan kalimat : ")
word = word.split()
bli = 0
ble = []
while bli in range(0,len(word)):
    bla = ((word[bli])[::-1])
    ble.append(bla)
    bli += 1
ble = " ".join(ble)
print (ble)

# # morse program
# morse = {"a":".- ", "b" : "-... ", "c":"-.-. ","d":"-.. ","e":". ","f":"..-. ","g":"--. ","h":".... ",
# "i":".. ", "j":".--- ","k":"-.- ","l":".-.. ","m":"-- ","n":"-. ","o":"--- ","p":".--. ","q":"--.- ",
# "r":".-. ","s":"... ","t":"- ","u":"..- ","v":"...- ","w":".-- ","x":"-..- ","y":"-.-- ",
# "z":"--.. ", " ":" / "}
# def conmors(x):
#     newString = ""
#     for i in x.lower():
#         newString += (morse.get(i))
#     print (newString)

# conmors(input("Masukkan kata yang akan diubah Morse : "))

# # CaesarCipher
# alfabet = list("abcdefghijklmnopqrstuvwxyz")
# def concaesar (kata, lgk):
#     rangkai = ""
#     for r in kata.lower():
#         if r in alfabet:
#             step = alfabet.index(r) + lgk
#             step = step % len(alfabet)
#             rangkai += alfabet[(step)]
#         else:
#             rangkai += " "
#     return (rangkai)

# print ("Caesar cipher akan mengganti karakter dalam kata menjadi karakter baru sesuai step yang anda inginkan...")
# kata = input("Masukkan kalimat : ")
# lgk = int(input("Masukkan step Caesar Cipher : "))
# print (f"Kalimat tersebut berubah menjadi \n {concaesar (kata, lgk)}")