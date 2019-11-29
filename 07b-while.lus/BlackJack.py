kaart = int(input('geef de kaart: '))
som = kaart
while kaart != 0 and som < 21:
    kaart = int(input('geef de kaart: '))
    som += kaart

if som == 21:
    print('Gewonnen!')
elif som < 21:
    print('Voorzichtig gespeeld (' + str(som) + ')')
else:
    print('Verbrand (' + str(som) + ')')
