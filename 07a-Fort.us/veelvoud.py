cijfer = int(input('geef cijfer: '))
som = 0
for veelvoud in range(cijfer, 101, cijfer):
    som += veelvoud

print(som)
