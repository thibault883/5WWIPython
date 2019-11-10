#invoer
kelvin = float(input('geef de temperatuur: '))
licht = float(input('geef de lichtsterkte: '))

#berekening
if licht > 10000:
    uitvoer = 'superreuzen (a)'
elif licht > 1000:
    uitvoer = 'superreuzen (b)'
elif 1000 > licht > 100 and kelvin < 7500:
    uitvoer = 'heldere reuzen'
elif 100 > licht > 10 and kelvin < 6000:
    uitvoer = 'reuzen'
elif licht < 0.01 and kelvin > 5000 or licht < 0.0001 and 5000 > kelvin > 3000:
    uitvoer = 'witte dwergen'
else:
    uitvoer = 'hoofdreeks'

print(uitvoer)
