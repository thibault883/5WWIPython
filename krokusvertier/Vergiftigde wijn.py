aantal = int(input('geef hoeveel dood: '))
fles = 0
for i in range(aantal):
    gevangen = input('geef de gevangene: ')
    fles += pow(2, ord(gevangen) - 65)

print('Fles #{} is vergiftigd.'.format(fles))
