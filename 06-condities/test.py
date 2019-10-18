getal = int(input('geef getal: '))

if getal < 0:
    if getal % 2 == 0:
        print('negatief even getal')
    else:
        print('negatief oneven getal')

elif getal > 0:
    if getal % 2 == 0:
        print('positief even getal')
    else:
        print('positief oneven getal')
else:
    print('getal is 0')
print('tot ziens')
