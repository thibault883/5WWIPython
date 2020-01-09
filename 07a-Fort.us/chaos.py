d = float(input('geef de populatiedichtheid: '))
r = float(input('geef de vruchtbaarheidsparameter: '))
s = int(input('geef de tijd: '))
print(d)
for i in range(s - 1):
    populatie = r * d * (1 - d)
    print(populatie)
    d = populatie
