getal_1 = int(input('geef een getal: '))
getal_2 = int(input('geef een getal: '))
som_1, som_2 = 0, 0
for i in range(1, getal_1):
    if getal_1 % i == 0:
        som_1 += i
for i in range(1, getal_2):
    if getal_2 % i == 0:
        som_2 += i

if som_1 == getal_2 and som_2 == getal_1:
    print('{:d} en {:d} zijn bevriende getallen'.format(getal_1, getal_2))
else:
    print('{:d} en {:d} zijn geen bevriende getallen'.format(getal_1, getal_2))
