#Cek hari apa X hari lagi/lalu
hari = [ "senin" , "selasa", "rabu", "kamis" , "jumat", "sabtu", "minggu"]
now = input("Hari apakah ini? ")
askQ = int(input("Mau cari berapa hari lagi (ketik 1) atau berapa hari lalu (ketik 2) : "))
def hariapa ():
    if askQ == 1:
        x = int(input("Berapa hari lagi : "))
        sisaHari = x % len(hari)
        hNow = hari.index(now.lower())
        xHari = (hari [(hNow + sisaHari) % len(hari)])
        return (f"Hari ini adalah hari {now.upper()}, maka {x} hari lagi adalah hari {xHari.upper()}")
    elif askQ == 2:
        x = int(input("Berapa hari lalu : "))
        sisaHari = x % len(hari)
        hNow = hari.index(now.lower())
        xHari = (hari [(hNow - sisaHari) % len(hari)])
        return (f"Hari ini adalah hari {now.upper()}, maka {x} hari lalu adalah hari {xHari.upper()}")
    else:
        return "Opsi pilihan salah!"

print (hariapa())