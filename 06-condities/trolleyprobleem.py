#invoer
ant_1 = str(input('geef antwoord: '))
ant_2 = str(input('geef tweede antwoord: '))

#berekening
if ant_1 != ant_2:
    uitvoer = 1
elif ant_1 == 'ja':
    uitvoer = 2
else:
    uitvoer = 5

#uivoer
print(uitvoer)
