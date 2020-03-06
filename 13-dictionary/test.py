fruitmand = {'kiwi': 4, 'banaan': 2, 8: 3}

for key, value in fruitmand.items():
    print(key, '-', value)

k = input('wat voeg je toe: ')
v = int(input('hoeveel: '))

if k in fruitmand:
    fruitmand[k] += v
else:
    fruitmand[k] = v
print(fruitmand)
