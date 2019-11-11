#Program cek waktu 
import datetime as hmm
x = hmm.datetime.now()

hariIndo = {
    "Monday": "Senin", "Tuesday":"Selasa" , "Wednesday": "Rabu",
    "Thursday": "Kamis", "Friday": "Jumat", "Saturday": "Sabtu", "Sunday": "Minggu"
}
bulanIndo = {
    "January": "Januari", "February":"Februari" , "March": "Maret",
    "April": "April", "May": "Mei", "June": "Juni", "July": "Juli",
    "August":"Agustus", "September":"September", "October":"Oktober",
    "November":"Nopember","December":"Desember"
}

class time:
    def __init__ (self):
        self.hari = (hariIndo.get(x.strftime("%A")))
        self.tanggal = x.strftime("%x")
        self.bulan = bulanIndo.get(x.strftime("%B"))
        self.tahun = x.strftime("%Y")
        self.jam = x.strftime("%H")
        self.menit = x.strftime("%M")
        self.detik = x.strftime("%S")

waktu = time()
print (waktu.tanggal)