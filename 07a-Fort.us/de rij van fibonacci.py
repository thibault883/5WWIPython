aantal = int(input('welk getal: '))
getal_1 = 1
getal_2 = 0

for i in range(aantal):
    som = getal_1 + getal_2
    getal_1 = som - getal_1
    getal_2 = som

print(som)
