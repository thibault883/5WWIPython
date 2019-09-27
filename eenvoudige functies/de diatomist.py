#invoer
r = float(input("geef de straal van de kleine cirkel: "))
R = float(input("geef de straal van de grote cirkel: "))

#berekening
n = int(0.83*(R**2 / r**2) - 1.9)

#uitvoer
print(n)
