#invoer
windsnelheid = int(input('geef de windsnelheid: '))

#berekening
if windsnelheid >= 250:
    print('categorie 5')
elif windsnelheid >= 210:
    print('categorie 4')
elif windsnelheid >= 178:
    print('categorie 3')
elif windsnelheid >= 154:
    print('categorie 2')
elif windsnelheid >= 119:
    print('categorie 1')
else:
    print('geen orkaan')



