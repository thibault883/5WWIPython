#invoer
Il = float(input("geef de kans op leven op een planeet in ons melkwegstelsel: "))
Fi = float(input("geef fractie planeten waar zich intelligent leven ontwikkelt: "))
L = int(input("geef gemiddelde levensduur van communicerende beschavingen in jaren: "))
R = 2
Fc = 0.2


#berekening
N = int(R * Il * Fi * Fc * L)

#uitvoer
print("samenlevingen in de melkweg waarmee we zouden kunnen communiceren:", N)
