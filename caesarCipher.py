# CaesarCipher
alfabet = list("abcdefghijklmnopqrstuvwxyz")
def concaesar (kata, lgk):
    rangkai = ""
    for r in kata.lower():
        if r in alfabet:
            step = alfabet.index(r) + lgk
            step = step % len(alfabet)
            rangkai += alfabet[(step)]
        else:
            rangkai += " "
    return (rangkai)

print ("Caesar cipher akan mengganti karakter dalam kata menjadi karakter baru sesuai step yang anda inginkan...")
kata = input("Masukkan kalimat : ")
lgk = int(input("Masukkan step Caesar Cipher : "))
print (f"Kalimat tersebut berubah menjadi \n {concaesar (kata, lgk)}")