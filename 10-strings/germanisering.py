#overloop alle letters van de string
    #indien de letter een spatie is
    #volgende letter wordt hoofdletter
def germaniseer(zin):
    nieuwe_zin = ''
    for i in range(0, len(zin)):
        if zin[i] == ' ':
            nieuwe_zin += ' ' + zin[i + 1].upper()
        elif zin[i - 1] != ' ':
            nieuwe_zin += zin[i]

    return nieuwe_zin

print(germaniseer('Dit is een test'))
