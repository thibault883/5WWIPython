def vlag(soort, kleur):
    uitvoer = ''
    for i in range(len(kleur)):
        if soort == 'verticaal':
            uitvoer += kleur[i] + ' | '
        else:
            uitvoer += kleur[i] + '\n' + '-\n'

    return uitvoer[:-3]

print(vlag('verticaal',('zwart', 'geel', 'rood')))

