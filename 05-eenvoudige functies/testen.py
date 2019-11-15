getal_1 = int(input('geef een getal: '))
getal_2 = int(input('geef een getal: '))

som = getal_1 + getal_2

uitvoer = '{:6d} + {:<6} = {:<6}'
print(uitvoer.format(getal_1, getal_2, som))
print(uitvoer.format(getal_1 * 10, getal_2 * 10, som *10))
print(uitvoer.format(getal_1 * 100, getal_2 * 100, som * 100))
print(uitvoer.format(getal_1 * 1000, getal_2 * 1000, som * 1000))
print(uitvoer.format(getal_1 * 10000, getal_2 * 10000, som * 10000))

