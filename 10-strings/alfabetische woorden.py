def positie_laagste_ascii(woord):
    vorig = woord[0]
    stap = 0
    for i in range(len(woord)):
        if ord(woord[i]) < ord(vorig):
            vorig = woord[i]
            stap = i

    return stap


def sorteer(woord):
    sorteer = woord
    uitkomst = ''
    for i in range(len(woord)):
        uitkomst += sorteer[(positie_laagste_ascii(sorteer))]
        sorteer = sorteer[:positie_laagste_ascii(sorteer)] + sorteer[positie_laagste_ascii(sorteer) + 1:]

    return uitkomst


