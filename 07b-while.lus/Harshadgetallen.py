getal = int(input("geef een getal: "))
som = 0

for cijfer in str(getal):
    som += int(cijfer)

if getal % som == 0:
    print(getal, 'is een Harshadgetal')
else:
    print(getal, "is geen Harshadgetal")


