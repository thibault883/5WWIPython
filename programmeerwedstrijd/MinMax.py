import system
file_i = open('invoer.txt')
file_0 = open('uitvoer.txt', 'w')


aantal_gevallen = int(input('aantal lijsten: '))
for i in range(1, aantal_gevallen + 1):
    lengte_lijst = int(input('lijst: '))
    lijst = []
    for _ in range(lengte_lijst):
        lijst.append(int(input('getal: ')))
    print(i, min(lijst), max(lijst))


