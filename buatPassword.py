password = "aiueo"
inputan = ""
coba = 0
batas = 3
lebih = False

while inputan != password:
    inputan = input("Ketik password : ")
    coba += 1
    if inputan != password:
        print (f"Password Salah! Percobaan ke- {coba}")
        if coba == batas:
            print ("KESEMPATAN HABIS COBA 5 MENIT LAGI!")
            break
    else:
        print("Password Benar!")

'''
CARA 2
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
'''