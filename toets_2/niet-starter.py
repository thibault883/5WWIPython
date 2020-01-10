getal = float(input('geef een getal tussen 0 en 1: '))
som, stap = 0, 0
maal = 2
while som < getal:
    stap += 1
    som += (1 / maal)
    maal *= 2

print(stap, som)
