#invoer
straal = float(input("geef de straal: "))
snelheid = float(input("geef de snelheid: "))
constante = 398600.4418 * pow(10, 9)
from math import pi, sqrt

#berekening
lengte = (constante * straal) / ((2 * constante) - (straal * pow(snelheid, 2)))
periode_eerst = 2 * pi * sqrt(pow(lengte, 3) / constante)
periode_dagen = periode_eerst // 86400
periode = periode_eerst % 86400

periode_uren = periode // 3600
periode %= 3600

periode_minuten = periode // 60

#uitvoer
print("grote as:", lengte, "meter")
print("periode:", periode_eerst,  "seconden")
print("periode: " + str(int(periode_dagen)) + " dagen, " + str(int(periode_uren)) + " uren en " + str(int(periode_minuten)) + " minuten")
