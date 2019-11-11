bla = input("Masukkan kata : ")
def palin (kata):
    if (kata[::-1]).lower() == kata.lower():
        return "adalah Palindrome"
    else:
        return "bukanlah Palindrome"

print (f"{bla} {palin(bla)}")