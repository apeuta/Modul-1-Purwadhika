angka1 = [1, 2, 9, 4, 5, 6, 7, 8, 3, 3]
angka2 = [1, 2, 10, 4, 5, 3, 7, 8, 9, 6, 6]

class Statistika:
    def rerata (self, x):
        y = sum(x) / len (x)
        return y
    def nilaiTengah (self, x):
        x.sort()
        if len(x)%2 == 0:
            y = (((x[int((len(x))/2)]) + (x[(int((len(x))/2))-1]))/2)
        else:
            y = (x[int((len(x))/2)])
        return y
    def modus (self, x):
        default = 0
        angka = 0
        for y in x:
            if x.count(y) > default:
                default = x.count(y)
                angka = y
        return angka

stat = Statistika()
print (stat.modus(angka1))
print (stat.nilaiTengah(angka2))
print (stat.rerata(angka1))