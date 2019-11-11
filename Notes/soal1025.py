
days = {
    "senin": "monday", "selasa":"tuesday" , "rabu": "wednesday",
    "kamis": "thursday", "jumat": "friday", "sabtu": "saturday", "minggu": "sunday"
}
# hari = input("Ketik nama hari : ")
# print (f"Bahasa Inggris dari {hari} adalah ...")
# print (days.get(hari))
# day = days.get(hari.lower(), "Tiada")
# print (f"{hari.upper()} = {day.upper()}")
dina = input ("Masukkan bahasa EN/ID ... ")
# print (days.keys())
#days_list = list(days.items())
#print (days_list [0][1])

#cara 1
'''
if dina == (days_list [0][1]):
    print (days_list[0][0])
elif dina == (days_list [0][0]):
    print (days_list[0][1])
elif dina == (days_list [1][0]):
    print (days_list[1][1])
elif dina == (days_list [1][1]):
    print (days_list[1][0])
elif dina == (days_list [2][0]):
    print (days_list[2][1])
elif dina == (days_list [2][1]):
    print (days_list[2][0])
elif dina == (days_list [3][0]):
    print (days_list[3][1])
elif dina == (days_list [3][1]):
    print (days_list[3][0])
elif dina == (days_list [4][1]):
    print (days_list[4][0])
elif dina == (days_list [4][0]):
    print (days_list[4][1])
elif dina == (days_list [5][0]):
    print (days_list[5][1])
elif dina == (days_list [6][1]):
    print (days_list[6][0])
elif dina == (days_list [6][0]):
    print (days_list[6][1])

'''
#cara2
hari = list(days)
day = list(days.values())
if dina.lower() in hari:
    print (f"Bhs Inggris {dina.lower()} adalah {days.get(dina)}")
else:
    idDay = hari[day.index(dina.lower())]
    print (f"Bhs Indonesia {dina.lower()} adalah {idDay}")
'''
nilai = int(input("Masukkan nilai ..."))

if (nilai >= 82):
    print ("A")
elif (nilai <82) and (nilai >=72): #bisa pakai range >> nilai in range (72,81)
    print ("B")
elif (nilai <72) and (nilai >=62):
    print ("C")
elif (nilai <62) and (nilai >=52):
    print ("D")
else:
    print ("E")
'''