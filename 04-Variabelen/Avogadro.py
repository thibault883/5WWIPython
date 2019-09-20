#invoer
hoeveelheid_deeltjes = float(input('geef het aantal deeltjes: '))
molaire_massa = 32.06
avogadro = 6.020 * 10**23

#berekening
massa = molaire_massa * hoeveelheid_deeltjes
aantal_deeltjes = hoeveelheid_deeltjes * avogadro

#uitvoer
print(massa)
print(aantal_deeltjes)

