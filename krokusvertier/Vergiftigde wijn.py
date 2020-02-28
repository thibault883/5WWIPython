aantal = int(input('geef hoeveel dood: '))
fles, nummer = 0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(aantal):
    gevangen = input('geef de gevangene: ')
    fles += pow(2, nummer[ord(gevangen) - 65])

print('Fles #{} is vergiftigd.'.format(fles))
