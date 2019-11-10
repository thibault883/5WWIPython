#aantal_woorden = int(input('Aantal woorden: '))
#zin = ''
#for _ in range(aantal_woorden):
# zin += input('Woord: ') + ' '
#print(zin)

ant_1 = input('geef antwoord: ')
ant_2 = input('geef antwoord: ')

if ant_1 == ant_2:
    uitvoer = 'onbeslist'
elif ant_1 == 'blad' and ant_2 == 'steen':
    uitvoer = 'speler 1 wint'
elif ant_1 == 'steen' and ant_2 == 'schaar':
    uitvoer = 'speler 1 wint'
elif ant_1 == 'schaar' and ant_2 == 'blad':
    uitvoer = 'speler 1 wint'
else:
    uitvoer = 'speler 2 wint'
print(uitvoer)
