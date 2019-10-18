getal = int(input('geef getal: '))

if getal < 0 and getal % 2 == 0:
    uitvoer = 'negatief en even getal'
elif getal < 0 and getal % 2 != 0:
    uitvoer = 'negatief en oneven getal'
elif getal > 0 and getal % 2 == 0:
    uitvoer = 'positief en even getal'
elif getal > 0 and getal % 2 != 0:
    uitvoer = 'positeif en oneven getal'
else:
    uitvoer = 'gelijk aan 0'

print(uitvoer)
