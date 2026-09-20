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
    geregsteerd_datum = []
    for dag in range(1,8):
        datum = input("Wat is de datum(daf-maand-jaar):")
        if datum == "":
            print("\033[91m"+"bye"+"\033[0m")
            break
        else:
            geregsteerd_datum.append(datum)

        temp_invoer= input(f"Wat is op dag {dag}  de temperatuur[C]:")
        if temp_invoer =="":
            print("\033[91m"+"bye"+"\033[0m")
            break
        else:
            temp_invoer = float(temp_invoer)

        wind_invoer= input(f"Wat is op dag {dag} de windsnelheid[m/s]:")
        if wind_invoer == "":
            print("\033[91m"+"bye"+"\033[0m")
            break
        else:
            wind_invoer = float(wind_invoer)

        vocht_invoer= input(f"Wat is op dag {dag} de vochtigheid[%]:")
        if vocht_invoer == "":
            print("\033[91m"+"bye"+"\033[0m")
            break
        else:
            vocht_invoer = float(vocht_invoer)



        geregsteerd_temp.append(float(temp_invoer))
        gimedeld = sum(geregsteerd_temp) / len(geregsteerd_temp)
        print("\033[94m"+"Het is",str(temp_invoer)+"C","("+ str(fahrenheit(temp_invoer))+"F"+")"+"\033[0m")
        print("\033[94m"+str(weerrapport(temp_invoer,wind_invoer,vocht_invoer))+"\033[0m")
        print("\033[94m"+"Gem.temp tot nu toe is"+"\033[0m",round(gimedeld,1))
        print("="*39)

    if len(geregsteerd_datum) >= 1:
        print("\033[93m"+"hier zijn al gereegsteerd datum(s)", "\n", str(geregsteerd_datum)+"\033[0m")
    else:
        print("\033[91m"+"Sorry, er is geen gereegsteerd datum(s) gevonden"+"\033[0m")


weerstation()