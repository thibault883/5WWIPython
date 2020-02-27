def volgende_rij(laag):
    nieuwe_laag = []
    for i in range(len(laag) - 1):
        if laag[i] == laag[i + 1]:
            nieuwe_laag.append(laag[i])
        else:
            if (laag[i] == 'R' and laag[i + 1] == 'Y') or (laag[i] == 'Y' and laag[i + 1] == 'R'):
                nieuwe_laag.append('G')
            elif (laag[i] == 'G' and laag[i + 1] == 'Y') or (laag[i] == 'Y' and laag[i + 1] == 'G'):
                nieuwe_laag.append('R')
            else:
                nieuwe_laag.append('Y')

    return nieuwe_laag

def driehoek(laag):
    nieuwe_laag = volgende_rij(laag)
    laag = [laag]
    while len(nieuwe_laag) != 0:
        laag.append(nieuwe_laag)
        nieuwe_laag = volgende_rij(laag[-1])

    return laag

def kleuren(kleur):
    kleur_g, kleur_r, kleur_y = 0, 0, 0
    for i in range(len(kleur)):
        for k in range(len(kleur[i])):
            if kleur[i][k] == 'G':
                kleur_g += 1
            elif kleur[i][k] == 'R':
                kleur_r += 1
            else:
                kleur_y += 1

    return kleur_g, kleur_r, kleur_y


