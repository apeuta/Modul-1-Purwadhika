# morse program
morse = {"a":".- ", "b" : "-... ", "c":"-.-. ","d":"-.. ","e":". ","f":"..-. ","g":"--. ","h":".... ",
"i":".. ", "j":".--- ","k":"-.- ","l":".-.. ","m":"-- ","n":"-. ","o":"--- ","p":".--. ","q":"--.- ",
"r":".-. ","s":"... ","t":"- ","u":"..- ","v":"...- ","w":".-- ","x":"-..- ","y":"-.-- ",
"z":"--.. ", " ":" / "}
def conmors(x):
    newString = ""
    for i in x.lower():
        newString += (morse.get(i))
    print (newString)

conmors(input("Masukkan kata yang akan diubah Morse : "))