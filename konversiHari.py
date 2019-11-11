#Dictionary hari
days = {
    "senin": "monday", "selasa":"tuesday" , "rabu": "wednesday",
    "kamis": "thursday", "jumat": "friday", "sabtu": "saturday", "minggu": "sunday"
}
#input hari/day
dina = input ("Masukkan bahasa EN/ID ... ")
hari = list(days)
day = list(days.values())
if dina.lower() in hari:
    print (f"Bhs Inggris {(dina.lower()).upper()} adalah {(days.get(dina)).upper()}")
else:
    idDay = hari[day.index(dina.lower())]
    print (f"Bhs Indonesia {(dina.lower()).upper()} adalah {idDay.upper()}")