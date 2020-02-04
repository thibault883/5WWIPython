def versleutel_woord(woord, aantal):
    woord = woord.upper()
    uitkomst = ''
    for i in range(len(woord)):
        uitkomst += chr(ord(woord[i]) + aantal)

    return uitkomst

def versleutel_zin(zin, aantal):
    zin = zin.upper()
    uitkomst = ''
    for i in range(len(zin)):
        if zin[i] == ' ':
            uitkomst += '@'
        elif chr(ord(zin[i]) + aantal) == '@':
            uitkomst += ' '
        else:
            uitkomst += versleutel_woord(zin[i], aantal)

    return uitkomst



print(versleutel_zin('Persoonsgevens van maar liefst 143 miljoen Amerikanen werden er gehackt.', 12))

