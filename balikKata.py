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