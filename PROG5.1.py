bestand = open("cijfers.txt", "r")
regels = bestand.readlines()

totaal = 0

for regel in regels:
    cijfer_tekst = regel.strip()
    totaal = totaal + float(cijfer_tekst)

bestand.close()

print(f"Het totaal is: {totaal:.2f}")