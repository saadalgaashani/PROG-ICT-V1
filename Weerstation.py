
def  fahrenheit(temp_celcius):
    f = 32 + 1.8 * temp_celcius
    return f

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    voele = temp_celcius - luchtvochtigheid / 100 * windsnelheid
    return voele

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    voel = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)
    if voel < 0 and windsnelheid > 10:
        return ("Het is heel koud en het stormt! Verwarming helemaal aan!")
    elif voel <0 and windsnelheid <= 10:
        return ("Het is behoorlijk koud! Verwarming aan op de benedenverdieping!")
    elif voel >= 0 and voel <10 and windsnelheid >12:
        return("Het is best koud en het waait; verwarming aan en roosters dicht!")
    elif voel >= 0 and voel < 10 and windsnelheid <= 12:
        return("Het is een beetje koud, elektrische kachel op de benedenverdieping aan!")
    elif voel >= 10 and voel < 22:
        return ("Heerlijk weer, niet te koud of te warm.")
    else:
        return ("Warm! Airco aan!")

def weerstation():
    for dag in range(1,8):
        temp_invoer= float(input(f"Wat is op dag {dag}  de temperatuur[C]:"))
        wind_invoer= float(input(f"Wat is op dag {dag} de windsnelheid[m/s]:"))
        vocht_invoer= float(input(f"Wat is op dag {dag} de vochtigheid[%]:"))
    if temp_invoer != "":
        break
    elif wind_invoer != "":
        pass
    elif vocht_invoer != "":
        pass












print(weerstation())