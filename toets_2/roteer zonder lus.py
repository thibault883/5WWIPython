def roteer(woord, aantal):
    uitkomst = ''
    for i in range(len(woord)):
        hoeveel_keer = (aantal + i) // len(woord)
        uitkomst += woord[i + aantal - (hoeveel_keer * len(woord))]

    return uitkomst


