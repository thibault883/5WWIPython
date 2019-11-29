getal = int(input('geef een getal: '))
i = 2
if getal == 1:
    print('1 is geen priemgetal')
else:
    while getal % i != 0 and i != getal:
        i += 1

    if i == getal:
        print(getal, 'is een priemgetal')
    else:
        print(getal, 'is geen priemgetal')


