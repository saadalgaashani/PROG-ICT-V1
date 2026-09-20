from builtins import sum


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
    geregsteerd_temp = []
    for dag in range(1,8):
        temp_invoer= input(f"Wat is op dag {dag}  de temperatuur[C]:")
        if temp_invoer =="":
            print("bye")
            break
        else:
            temp_invoer = float(temp_invoer)

        wind_invoer= input(f"Wat is op dag {dag} de windsnelheid[m/s]:")
        if wind_invoer == "":
            print("bye")
            break
        else:
            wind_invoer = float(wind_invoer)

        vocht_invoer= input(f"Wat is op dag {dag} de vochtigheid[%]:")
        if vocht_invoer == "":
            print("bye")
            break
        else:
            vocht_invoer = float(vocht_invoer)

        geregsteerd_temp.append(float(temp_invoer))
        gimedeld = sum(geregsteerd_temp) / len(geregsteerd_temp)
        print("Het is",str(temp_invoer)+"C","("+ str(fahrenheit(temp_invoer))+"F"+")")
        print(weerrapport(temp_invoer,wind_invoer,vocht_invoer))
        print("Gem.temp tot nu toe is",round(gimedeld,1))
        print("="*39)













weerstation()