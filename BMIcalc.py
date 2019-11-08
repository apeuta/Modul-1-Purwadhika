#BMI calculator
massa = int(input("Masukkan massa (kg) : "))
tinggi = int(input ("Masukkan tinggi (cm) : "))
Indeks = massa / (tinggi/100) ** 2

print (f"Jika berat anda {massa} kg dan tinggi anda {tinggi} cm, maka ...")
if (Indeks < 18.5):
    print ("Berat badan anda kurang")
elif (Indeks >= 18.5 and Indeks< 25):
    print ("Berat badan anda ideal")
elif (Indeks >= 25 and Indeks<30):
    print ("Berat badan anda berlebih")
else:
    print ("Berat badan anda sangat berlebih")