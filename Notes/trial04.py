# angka = 1
# while (angka<=10):
#     print (angka)
#     angka+=1

# z = ""
# for item in range (5):
#     for item1 in range (0, item + 5):
#         z.remove ("* ")
#     z += "\n"

# print (z)

#dictionary
andi = {
    "name" : "Andi",
    "age" : 22,
    "is_married": False,
    "job": "PNS",
    "address" : {
        "street": "Mawar Ungu",
        "RT": 5, "RW": 3, "kecamatan" : "Indiana",
        "zipcode" : 12345,
        "geo" :{
            "lat": 111.11,
            "lng": 65.89
        }
    }
}
# print (andi["name"])
# print (andi["age"])
# print (andi["is_married"])
# print (andi.get("job")) #untuk yg tidak ada di dictionary lebih baik pakai get
'''
andi["name"] = "Budi"
# print (andi)
# print (andi["address"]["geo"])
andi["salary"] = 5000000
andi.update({"no_ktp" : 3333330101010000})
andi["address"].update({"no_rumah" : 10})
print (andi)
print (andi.keys()) #masih bukan list
print (andi.values())
'''
# x = 4

# if x == 4:
#     print ("Ini 4")
# else:
#     print ("Bukan4")

'''
Comparison
x =< kurang dari sama dengan 
x >= lebih dari sama dengan
x != tidak sama dengan
= False kalau boolean, bisa ditulis -not- saja
and untuk menggabungkan kondisi
'''
'''
x = True
y = False

if x and y:
    print ("Anda x dan y")
elif x and not y:
    print ("Anda x")
elif not x and y:
    print ("Anda y")
else:
    print ("Sopo kowe?")
'''
