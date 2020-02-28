def graad(woord):
    slinger, aantal = woord[0], 0

    while slinger in woord[len(woord) // 2:]:
        aantal += 1
        slinger += woord[aantal]

    return aantal

def slinger(woord, keer):
