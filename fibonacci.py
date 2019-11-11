class fibo():
    def __init__(self,indeks):
        self.indeks = indeks
    def fibolist(self):
        deret = [0,1]
        for i in range (2, self.indeks +1):
            deret.append(deret[i-2] + deret [i-1])
        print (deret[1:])
        return deret[self.indeks]
inputan = int(input("Deret fibonacci keberapa yang ingin anda ketahui angkanya : "))
fibo = fibo(inputan)
print (f"Deret fibonacci ke-{inputan} adalah {fibo.fibolist()}")