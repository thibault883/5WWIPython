#invoer
T = float(input("geef de luchttemperatuur in °C: "))
W = float(input("geef de windsnelheid in km/u: "))

#berekening
gevoelstemperatuur = 13.12 + 0.6215 * T + ((0.3965 * T) - 11.37) * (W)**0.16

#uitvoer
print(gevoelstemperatuur)
