#invoer
t = int(input("geef de tijd: "))
c = 299792458
n = 1.000277

#berekening
d = (c * t * 10**-9) / (2 * n)
#uitvoer
print(d,"meter")
