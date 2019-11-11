'''
Bilangan Prima 1-100
'''
nomor = list (range (1,101))
#Cara 1
prima = list(filter(lambda x : x % 7 or x == 7, 
filter (lambda x: x % 5 or x == 5, 
filter(lambda x: x % 3 or x == 3, 
filter(lambda x: x % 2 or x == 2, 
filter (lambda x : x>1, nomor))))))

print (f"Jumlah bilangan prima dari 1-100 adalah {len(prima)}")
print (prima)

#Cara 2
prime = list(filter (lambda x :(x % 7  or x == 7) and (x % 5  or x == 5) and 
(x % 3  or x==3) and (x % 2  or x == 2) and (x > 1) , nomor))
print (prime)

#Cara 3
def primus (x):
    a = False
    if x > 1:
        if x == 2: a = True
        else:
            for i in range (2, x):
                if x % i == 0: a = False; break
                else: a = True
    else: a = False
    return a

z = list (filter(primus, range(101)))
print (z)