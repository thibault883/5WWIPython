# invoer
r = float(input('geef de afstand: '))
r = r * 10**-2
Q1 = 2.0 * 10**-6
Q2 = 1.0 * 10**-6
k = 8.99 * 10**9

#berekening
Fc = (k * Q1 *Q2) / r**2

# uitvoer
print(Fc)
