#invoer
straal_klein = float(input("geef de straal van de kleine cirkel: "))
straal_groot = float(input("geef de straal van de grote cirkel: "))

from math import pi, floor
#berekening

aantal_cirkel = floor(0.83*(pow(straal_groot, 2) / pow(straal_klein, 2)) - 1.9)
opp_bedekt = (aantal_cirkel * pow(straal_klein, 2) * pi) / (pow(straal_groot, 2) * pi) * 100

#uitvoer
uitvoer = "{:d} kleine cirkels bedekken {:.2f}% van de grote cirkel"
print(uitvoer.format(aantal_cirkel, opp_bedekt))
