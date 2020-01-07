aantal_keer = int(input('geef het aantal: '))
som, som_vorig = 1, 0

for i in range(aantal_keer - 1):
    vorig = som_vorig
    som_vorig = som
    som = vorig + som_vorig

print(som)
