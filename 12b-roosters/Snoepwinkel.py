from operator import itemgetter

def bereken_prijs(lijst):
    prijs = 0
    for i in range(len(lijst)):
        prijs += lijst[i][1]

    return prijs

def winkelbriefje(lijst):
    winkel = []
    for i in range(len(lijst)):
        winkel += [lijst[i][0]]

    return winkel

def sorteer(lijst):
    lijst.sort(key=itemgetter(1))

    return lijst
