geld = int(input('hoeveel geld heb je: '))
inzet = input('hoeveel geld zet je in: ')
inzet_2 = ''
if inzet == 'alles':
    inzet = geld

while inzet != 'stop' and int(inzet) <= geld:
    inzet = int(inzet)
    kleur_1 = input('welk kleur kies je: ')
    kleur_2 = input('het kleur is: ')
    geld -= int(inzet)
    if kleur_1 == kleur_2:
        inzet *= 2
    else:
        inzet = 0
    geld += inzet
    inzet = input('hoeveel geld zet je in: ')
    if inzet == 'alles':
        inzet = geld
while inzet != 'stop' and inzet_2 != 'stop':
    kleur_1 = input('welk kleur kies je: ')
    kleur_2 = input('het kleur is: ')
    inzet_2 = input('hoeveel geld zet je in: ')
if geld == 0:
    print('Je eindigt met {} dollar.'.format(geld))
elif inzet != 'stop':
    print('Je kunt geen {} dollar inzetten als je maar {} dollar hebt.'.format(int(inzet), geld))
else:
    print('Je eindigt met {} dollar.'.format(geld))
