def ontdubbelen(woord):
    uitkomst = ''
    vorige_letter = ''
    for i in range(len(woord)):
        if woord[i] != vorige_letter:
            uitkomst += woord[i]
        vorige_letter = woord[i]

    return uitkomst

print(ontdubbelen('aaien'))
