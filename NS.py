# Bronnen: lesmateriaal en programmeerassistent voor controle
def standaardprijs(afstandKM):
    if afstandKM <= 0:
        return  0
    elif afstandKM <= 50 :
        return afstandKM * 0.80
    elif afstandKM > 50:
        return afstandKM * 0.60 +15

def ritprijs(leeftijd, weekendrit, afstandKM):

        basis_prijs = standaardprijs(afstandKM)

        if (weekendrit == False) and (leeftijd < 12 or leeftijd >= 65):
            return basis_prijs * 0.70 ## [0,56] 50(28), 55(33.599999999999994)

        elif (weekendrit == True) and (leeftijd < 12 or leeftijd >= 65) :
            return basis_prijs * 0.65 ## [0,52] 50(26), 55 (31.200000000000003)

        else:
            ## hier is de korting voor de overige leeftijdsgroepen
            if weekendrit == True:
                 return basis_prijs * 0.60 # [0,48] 50(24), 55(28.799999999999997)
            else:
                 return basis_prijs

kort = ritprijs(15,False,55)

print("--- Test 1: Standaardprijs ---")
print("Afstand -10 km (moet 0 zijn):", standaardprijs(-10))
print("Afstand 0 km   (moet 0 zijn):", standaardprijs(0))
print("Afstand 30 km  (moet 24.0 zijn):", standaardprijs(30))
print("Afstand 50 km  (moet 40.0 zijn):", standaardprijs(50))
print("Afstand 60 km  (moet 51.0 zijn):", standaardprijs(60))

print("\n--- Test 2: Ritprijs (Doordeweeks / False) ---")
print("Kind 11 jr, doordeweeks, 50 km (moet 28.0 zijn):", ritprijs(11, False, 50))
print("Volwassene 20 jr, doordeweeks, 50 km (moet 40.0 zijn):", ritprijs(20, False, 50))
print("Senior 65 jr, doordeweeks, 50 km (moet 28.0 zijn):", ritprijs(65, False, 50))

print("\n--- Test 3: Ritprijs (Weekend / True) ---")
print("Kind 11 jr, weekend, 50 km (moet 26.0 zijn):", ritprijs(11, True, 50))
print("Volwassene 20 jr, weekend, 50 km (moet 24.0 zijn):", ritprijs(20, True, 50))
print("Senior 65 jr, weekend, 50 km (moet 26.0 zijn):", ritprijs(65, True, 50))

print("\n--- Test 4: Randgevallen leeftijd ---")
print("Persoon precies 12 jr, doordeweeks, 50 km (moet 40.0 zijn):", ritprijs(12, False, 50))
print("Persoon precies 12 jr, weekend, 50 km (moet 24.0 zijn):", ritprijs(12, True, 50))