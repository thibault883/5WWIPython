#invoer
punt_thuis = int(input('geef de punten van de thuisploeg: '))
punt_uit = int(input('geef de punten van de uitploeg: '))

#berekening
verschil = abs(punt_thuis - punt_uit)

if verschil >= 20:
    winnaar = 800
    verliezer = 200
elif verschil >= 10:
    winnaar = 700
    verliezer = 300
else:
    winnaar = 600
    verliezer = 400

if punt_thuis > punt_uit:
    punt_thuis = winnaar
    punt_uit = verliezer
else:
    punt_thuis = verliezer
    punt_uit = winnaar

punt_uit += 70
punt_thuis -= 70

#uitvoer
print('thuisploeg: {:.2f}'.format(punt_thuis))
print('  uitploeg: {:.2f}'.format(punt_uit))
