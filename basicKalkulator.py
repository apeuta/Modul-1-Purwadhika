#function basic calculator

def kalk():
    a = float(input("Masukkan angka 1 : "))
    x1 = (input("Masukkan operator aritmatika (+-*/) : "))
    b = float(input("Masukkan angka 2 : "))
    if x1 == "+":
        print (a + b)
    elif x1 == "-":
        print (a - b)
    elif x1 == "*":
        print (a * b)
    elif x1 == "/":
        print (a / b)
    else:
        print ("Maaf operator tidak dikenali")

kalk()