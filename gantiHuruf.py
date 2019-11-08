#Ganti huruf tanpa replace
hurufvokal = list ("aiueo")
def gantio(x):
    newString = ""
    o = input("Masukkan huruf vokal pengganti : ")
    for i in x.lower():
        if i in hurufvokal:
            newString += o
        else:
            newString += i
    print (newString) 

gantio(input("Masukkan kata/kalimat yang huruf vokalnya akan diganti : "))