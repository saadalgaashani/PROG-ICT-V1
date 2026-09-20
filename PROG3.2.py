leeftijd = int(input("schrijf je leeftijd in:"))

pasport = input("heb je de Nederlands paspoort (ja/nee): ")

if leeftijd >= 18 and pasport == "ja":
    print("je mag stemmen")

else:
    print("je mag niet stemmen")