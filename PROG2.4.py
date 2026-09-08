import random

prijs = random.randint(10,150)
print("De prijs van het gekozen product:" ,prijs)
betaald = input("Het betaalde bedrag:")

rekennen = (int(betaald) - prijs)

munt_50 = rekennen // 50
rest = rekennen % 50
print("aantal munten van 50 eurocent is" ,munt_50)

munt_20 = rest // 20
rest = rest % 20
print("aantal munten van 20 eurocent is",munt_20)

munt_10 = rest // 10
rest = rest % 10
print("aantal munten van 10 eurocent is",munt_10)

munt_5 = rest // 5
rest = rest % 5
print("aantal munten van 5 eurocent is",munt_5)

munt_2 = rest // 2
rest = rest % 2
print("aantal munten van 2 eurocent is",munt_2)

munt_1 = rest // 1
rest = rest % 1
print("aantal munten van 1 eurocent is",munt_1)

print("intotaal :",rekennen,"cent")