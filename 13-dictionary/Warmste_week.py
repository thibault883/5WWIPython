def gift_inschrijven(klas, bedragen):
    if klas[0] in bedragen:
        bedragen[klas[0]] += klas[1]
    else:
        bedragen[klas[0]] = klas[1]

    return bedragen

