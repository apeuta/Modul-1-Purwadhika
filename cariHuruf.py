#Program cari huruf/kata tanpa count
teks = input("Tuliskan kalimat : ")
cariHuruf = input("Masukkan huruf/kata yang ingin anda cari? ")
abc = teks.lower().replace(cariHuruf,"")
jmlCari = len(teks) - len(abc)
print (f"Jumlah huruf {cariHuruf} di dalam kalimat adalah ...")
print (jmlCari)

#Dengan count
print (teks.lower().count(cariHuruf))