maandnu = int(input("schrijf je maandnummer:"))

if maandnu <1 or maandnu >= 13:
    print("ongeldig")
elif maandnu>= 3 or maandnu<=5 :
    print("lente")
elif maandnu >= 9 or maandnu <= 11:
    print("herfst")
else:
    print("jij bent bebeuren in de winter")