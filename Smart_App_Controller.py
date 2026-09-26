def aantal_dagen(inputFile):
    bestand = open("dagen.txt","r")
    regels = bestand.readlines()
    print(f"aantal regels:{len(regels)}")
    for regel in regels:
        print(len(regel))
    bestand.close()
    return bestand




def auto_bereken(inputFile, outputFile):
    pass

def overwrite_settings(outputFile):
    pass
def smart_app_controller():
    pass

print(aantal_dagen())