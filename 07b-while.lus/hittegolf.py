temperatuur = input('geef de temperatuur: ')
eind = 2
while temperatuur != 'stop' and eind != 1:
    aantal_25, aantal_30 = 0, 0
    while str(temperatuur) != 'stop' and float(temperatuur) < 25:
        temperatuur = input('geef de temperatuur: ')

    while str(temperatuur) != 'stop' and float(temperatuur) >= 25:
        aantal_25 += 1
        if float(temperatuur) >= 30:
            aantal_30 += 1
        temperatuur = input('geef de temperatuur: ')

    while str(temperatuur) != 'stop' and float(temperatuur) <= 25:
        temperatuur = input('geef de temperatuur: ')

    if aantal_25 >= 5 and aantal_30 >= 3:
        eind = 1
    else:
        eind = 2

if eind == 1:
    print('hittegolf')
else:
    print('geen hittegolf')
