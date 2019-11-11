'''
Ubah Karakter
aBcDEFghi -> AbCdefGHI
'''
def uplow(x):
    y = list(x)
    z = []
    for i in y:
        if i == i.upper():
            z.append(i.lower())
        else:
            z.append(i.upper())
    print ("".join(z))
kata = input("Masukkan kata dengan gabungan uppercase dan lowercase : ")
uplow(kata)