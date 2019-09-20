#invoer
eurocent = y = int(input('Geef aantal eurocent: '))

#berekening
aantal_muntstukken = eurocent // 100
eurocent = eurocent % 100

aantal_muntstukken += (eurocent // 50)
eurocent = eurocent % 50

aantal_muntstukken += (eurocent // 20)
eurocent = eurocent % 20

aantal_muntstukken += (eurocent // 10)
eurocent = eurocent % 10

aantal_muntstukken += (eurocent // 5)
eurocent = eurocent % 5

aantal_muntstukken += (eurocent // 2)
eurocent = eurocent % 2

aantal_muntstukken += (eurocent // 1)
eurocent = eurocent % 1

# uitvoer
print(y,'cent kan je omwisselen in', aantal_muntstukken,'muntstukken' )
