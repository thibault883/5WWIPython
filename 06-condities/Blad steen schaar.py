#invoer
ant_1 = str(input('geef jouw antwoord: '))
ant_2 = str(input('geef jouw antwoord: '))

#berekening
if ant_1 == ant_2:
    uitvoer = 'onbeslist'
elif ant_1 == 'blad':
    if ant_2 == 'steen':
        uitvoer = 'speler 1 wint'
    else:
        uitvoer = 'speler 2 wint'
elif ant_1 == 'steen':
    if ant_2 == 'schaar':
        uitvoer = 'speler 1 wint'
    else:
        uitvoer = 'speler 2 wint'
else:
    if ant_2 == 'blad':
        uitvoer = 'speler 1 wint'
    else:
        uitvoer = 'speler 2 wint'

#uitvoer
print(uitvoer)
