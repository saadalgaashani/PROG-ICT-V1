#
# x = 5
# y = 8
#
# if x > y :
#     print ("x is greater then y")
# else:
#     print("else is not greater then y")
# x = 9
# y = 4
# z = 13
#
# voornaam = "saad"
#
# if 14 > x+y:
#  if x+y == z:
#   if x/y < z or x/y >10:
#    if len(voornaam) > y:
#     print("je hebt")
#
# ##sd = int(input("schrijf je nummer:"))
#
# ##print(sd**2)    ##schrijf het antwoord liever op een variabale om het te opslaaan
#
# cv = [1,2,4,5,6,7]
#
# sum(cv) / len(cv)  ## zo maak je hetgemidelde van de lijst
# around = 1.2325
# dec = 2
# ##print(round(around,dec))
#
# dfdf =  [1,3,4,5,6]
#
# gim = sum(dfdf) / len(dfdf)
#
# print(gim)



# x = 9
# y = 4
# z = 13
#
# voornaam = "saad"
#
# if 14 > x+y:
#  if x+y == z:
#   if x/y < z or x/y >10:
#    if len(voornaam) > y:
#     print("je hebt")

##sd = int(input("schrijf je nummer:"))

##print(sd**2)    ##schrijf het antwoord liever op een variabale om het te opslaaan

# cv = [1,2,4,5,6,7]
#
# sum(cv) / len(cv)  ## zo maak je hetgemidelde van de lijst
# around = 1.2325
# dec = 2
# ##print(round(around,dec))
#
# dfdf =  [1,3,4,5,6]
#
# gim = sum(dfdf) / len(dfdf)
#
# print(gim)

# num = 1
# while num <= 9:
#     print(num)
#     num += 2
# print("Klaar")

# sum = []

# matrix_bord = [
# [0, 1, 1, 1, 0],
# [1, 0, 0, 0, 1],
# [1, 0, 0, 0, 1],
# [1, 0, 0, 0, 1],
# [0, 1, 1, 1, 0]
# ]
#
# for rij in matrix_bord:
#     for lampje in rij:
#         if lampje ==0:
#             print(" ",end="")
#         else:
#             print("0",end="")
#     print()

# fruitmand = {"appel":3,"banaan":5,"kers":50}
#
# print(fruitmand["banaan"] * fruitmand["appel"])
#
# if "mango" in fruitmand:
#     print(fruitmand["mango"])

# fruitmand = {"appel":3,"banaan":5}
# fruitmand["mango"]= int(input("hoeveel mango's"))
# print(fruitmand)
# fruitmand["mango"]= 4
# print(fruitmand,end="\n\n")
#
# for key in fruitmand:
#     print(key,"=",fruitmand[key])
#



# telegboek = {"Saad":123456789,"Jurjan":987654321}
#
# telegboek["melle"] = 897654321
# telegboek[input("schrijf de naam:")] = int(input("schrijf het nummer:"))
# for tel in telegboek:
#     print(tel, "=",telegboek[tel])


#
# fruitmand = {"appel":3, "banaan":5, "kers":50}
#
# print("Aantal fruitsoorten: ", len(fruitmand.keys()))
# print("Aantal vruchten: ", sum(fruitmand.values()))
#
# print("Voldoende voorraad van:")
#
# for key, value in fruitmand.items():
#     if value > 10:
#         print(key, ":", value)

# fruitmand = {"appel": 3, "banaan": 5}
# peren = fruitmand.get("peer")
#
#     if peren:
#         print("peren:", 0)
#     else:
#         print("peren:", peren)

telegboek = {"Saad":123456789,"Jurjan":987654321}
# naam = input("Wie zoekt u? ")
# nummer = telegboek.get(naam, 'werd niet gevonden')
zoeknummer = input("welk nummer zoekt u e? ")
if zoeknummer not in telegboek.keys():
    print("Dit nummer is onbekend!")
else:
    for naam,nummer in telegboek.items():
        if naam == zoeknummer:
            print("Dit naam is van",nummer)
#
#
#
# fruitmand = {"appel": 3, "banaan": 5,"kers":50}
#
# verwijderd = fruitmand.pop("appel")
# del fruitmand["kers"]
# print(fruitmand)
# print(verwijderd)