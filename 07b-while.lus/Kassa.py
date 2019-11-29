getal = float(input('geef de prijs: '))
prijs = getal
while getal != 0:
    getal = float(input('geef de prijs: '))
    prijs += getal

uitvoer = 'De totale prijs is € {:.2f}'
print(uitvoer.format(prijs))
