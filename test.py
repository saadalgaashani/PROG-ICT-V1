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

matrix_bord = [
[0, 1, 1, 1, 0],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[0, 1, 1, 1, 0]
]

for rij in matrix_bord:
    for lampje in rij:
        if lampje ==0:
            print(" ",end="")
        else:
            print("0",end="")
    print()