def graad(woord):
    slinger, aantal = woord[0], 0

    while slinger in woord[len(woord) // 2:]:
        aantal += 1
        slinger += woord[aantal]

    return aantal

def slinger(woord, keer):
    if graad(woord) != 0 and keer != 0:
        uitvoer = (woord[:-graad(woord)] * keer) + woord[:graad(woord)]
    else:
        uitvoer = woord * keer

    return uitvoer


