
def kwadraten_som(grondgetallen):
    totaal = 0
    for getal in grondgetallen:
        if getal > 0 :
            totaal = totaal + getal **2

    return totaal
print(kwadraten_som([4,3,-5]))