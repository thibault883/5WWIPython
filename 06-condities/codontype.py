#invoer
soort = input('geef het codon: ')

#berekening
if soort == 'AUG':
    uitvoer = 'start codon'
elif soort == 'UAG' or soort == 'UGA' or soort == 'UAA':
    uitvoer = 'stop codon'
elif len(soort) != 3:
    uitvoer = 'ongeldig codon'
else:
    uitvoer = 'gewoon codon'
print('Het codon', soort, 'is een', uitvoer + '.')
