eiwit = input()
m = int(input())
aantal = int(input())
aantal_afwijking = 0
for i in range(aantal):
    h = 0
    afwijking = input()
    for k in range(len(afwijking)):
        if afwijking[k] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and h != 1:
            getal = int(afwijking[:k])
            letter = afwijking[k:]
            h = 1
            if eiwit[getal - 1] in letter:
                aantal_afwijking += 1

if aantal_afwijking >= m:
    diagnose = 'positief'
else:
    diagnose = 'negatief'

print('{} ({})'.format(diagnose, aantal_afwijking))
