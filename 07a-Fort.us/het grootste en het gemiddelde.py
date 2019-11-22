aantal_keer = int(input('hoeveel getallen: '))

#lees het eerste getal voor de lus in
getal_0 = int(input('geef getal: '))

#het eerste getal is onmiddellijk de som en het grootste getal
gemiddelde, grootste = getal_0, getal_0

for i in range(aantal_keer - 1):
    getal = int(input('geef getal: '))
    gemiddelde += getal
    grootste = max(grootste, getal)


uitvoer = 'Het grootste getal is {} en het gemiddelde is {:.2f}'
print(uitvoer.format(grootste, gemiddelde / aantal_keer))

