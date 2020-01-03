snel_s = int(input('geef de snelheid van Stijn: '))
snel_k = int(input('geef de snelheid van Kaat: '))
afstand = int(input('geef de afstand: '))
tijd, som_s, som_k = 0, 0, 0

while som_s + som_k < afstand:
    som_s += snel_s
    som_k += snel_k
    tijd += 1

print("Na", tijd, "s hebben Stijn en Kaat elkaar ontmoet.")
