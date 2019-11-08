#Program ubah hari ke tahun, bulan, dan hari
hari1 = int(input("Masukkan jumlah hari : "))
tahun = round(hari1/365)
bulan1 = (hari1 % 365)
bulan = round(bulan1 / 30)
hari = (bulan1 % 30)
print (f"{hari1} hari adalah {tahun} tahun, {bulan} bulan, dan {hari} hari")