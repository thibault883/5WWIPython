#invoer
straal_klein = float(input("geef de straal van de kleine cirkel: "))
straal_groot = float(input("geef de straal van de grote cirkel: "))

#berekening
n = int(0.83*(pow(straal_groot, 2) / pow(straal_klein, 2)) - 1.9)

#uitvoer
print(n)
