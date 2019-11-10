#invoer
hoed_1 = input('geef de kleur: ')
hoed_2 = input('geef de kleur: ')
persoon = int(input('geef de persoon: '))

#berekening
if persoon == 1:
    uitvoer_2 = hoed_1
    if hoed_2 == 'wit':
        uitvoer_1 = 'zwart'
    elif hoed_2 == 'zwart':
        uitvoer_1 = 'wit'
else:
    uitvoer_1 = hoed_2
    if hoed_1 == 'wit':
        uitvoer_2 = 'zwart'
    elif hoed_1 == 'zwart':
        uitvoer_2 = 'wit'

print(uitvoer_1)
print(uitvoer_2)
