'''
Diketahui
S = {bilangan cacah kurang dari 11}
A = {x|x < 10, x E bilangan prima}
B = {5, 7, 9}
Tentukan :
A
B
(A n B)
(A u B)
A n ( A u B)
B n (A u B)
(A u B) n (A u B)
(A n B) u (A u B)
'''
S = []
A = set([2,3,5,7])
B = set([5,7,9])

for i in range (0,11):
    S.append(i)
S = set(S)

print (A)
print (B)
print (A & B)
print (A | B)
print (A & (A | B))
print (B & (A | B))
print ((A | B) & (A | B))
print ((A & B) | (A | B))
