'''
Membuat Angka ke Romawi
'''
RomNum = {"M" : 1000, "CM" : 900, "D": 500, "CD": 400, "C" : 100, "XC" : 90,
 "L": 50, "XL":40,"X": 10, "IX": 9, "V": 5, "IV":4, "I": 1}
Romawi = list (RomNum)
Numeral = list (RomNum.values())
bla = []
def Ubah(a):
    while a > 0:
        for i in range (0,len(RomNum)):
            if a >= Numeral[i]:
                bla.append(Romawi[i] * (int(a / Numeral[i])))
                a %= Numeral[i]
                i+= 1
    return "".join(bla)

print (Ubah(3424))