'''
x = "hahaha"    #cek upper atau lower by Boolean
print(x.islower())
print(x.isupper())

print (len(x))

# [start : stop : step]
print (x [0:3])  #seleksi karakter
print (x [-1] ) #paling belakang
print (x[len(x) - 1])

print (x.index("a"))   #hitung a di karakter berapa
print (x.replace("a", "e")) #ganti karakter

print (len(x.replace(" ", "")))    #hitung karakter tanpa spasi

print (x.count('ha'))   #hitung karakter h di x
cari = "h"
print(cari.lower() in x.lower())
print(x.lower().count(cari.lower()))

nama = "Andra Pranata Utama"
print (len(nama))
print (x [-1])
'''
#list
hari = [ "Senin" , "Selasa", "Rabu", "Kamis" , "Jumat", "Sabtu", "Minggu"]
'''
Sekarang hari Rabu, hari apa 100 hari lagi?
'''
# now = input("Hari apakah ini? ")
# brpHari1 = int(input("Berapa hari lagi : "))
# brpHari2 = int(input("Berapa hari lalu : "))

# sisaHari1 = brpHari1 % len(hari)
# hNow1 = hari.index(now)
# lagiHari = (hari [(hNow1 + sisaHari1) % len(hari)])

# sisaHari2 = brpHari2 % len(hari)
# hNow2 = hari.index(now)
# laluHari = (hari [(hNow2 - sisaHari2) % len(hari)])
# print (f"Hari ini adalah {now}, {brpHari1} hari lagi adalah hari {lagiHari} dan {brpHari2} hari lalu adalah hari {laluHari}")

'''
append = menambahkan data
insert = menyisipkan data
remove = menghilangkan data
pop = mengurangi data 
sort = mengurutkan a-z
sort(reverse = True) = mengurutkan z-a
reverse = membalik urutan data

variabel.append (data baru)
variabel.insert (index, data baru)
variabel.remove (data baru)
variabel.pop () >> data terakhir
variabel.pop (index) >> data ke index
variabel.sort ()
variabel.reverse ()
variabel = variable [: : -1]
'''

z = [
    [1 , 2 , 3],
    [4, 5, 6],
    [7, 8 ,9]
]
# print (z [1] )
# print (z [2][2])
'''
#result
[4, 5, 6]
9
'''