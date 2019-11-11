#Program hitung hewan
jumlahKaki = int(input("Berapa jumlah total kaki? "))
jumlahEkor = int(input ("Berapa jumlah ekor? "))
kakiAyam = int(input ("Berapa jumlah kaki hewan A? "))
kakiKambing = int(input ("Berapa jumlah kaki hewan B? "))

div = abs(kakiKambing-kakiAyam)
if div == 0:
    div = 1

Ayam = abs((jumlahKaki - (jumlahEkor*kakiKambing)))/div
Kambing = jumlahEkor - Ayam
print ("Jumlah hewan A adalah")
print (Ayam)
print ("Jumlah hewan B adalah")
print (Kambing)