nilai = int(input("Masukkan nilai : "))

if (nilai >= 82):
    print (f"Nilai {nilai} = A")
elif (nilai <82) and (nilai >=72): #bisa pakai range >> nilai in range (72,81)
    print (f"Nilai {nilai} = B")
elif (nilai <72) and (nilai >=62):
    print (f"Nilai {nilai} = C")
elif (nilai <62) and (nilai >=52):
    print (f"Nilai {nilai} = D")
else:
    print (f"Nilai {nilai} = E")