aantal_keer = int(input('hoeveel getallen: '))

gemiddelde = 0
max = -100
for i in range(aantal_keer):
    getal = int(input('geef getal: '))
    gemiddelde += getal
    if getal >= max:
        max = getal

uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'
print(uitvoer.format(max, gemiddelde / aantal_keer))

