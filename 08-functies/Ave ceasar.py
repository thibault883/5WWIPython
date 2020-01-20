def is_letter(t):
    return ord('a') <= ord(t) <= ord('z') or ord('A') <= ord(t) <= ord('Z')

def roteer_letter(t, aantal):
    if str(is_letter(t)) == 'True':
        letter = ord(t) + aantal
        if ord('a') <= ord(t) <= ord('z'):
            if not ord('a') <= letter <= ord('z'):
                letter -= 26
        elif ord('A') <= ord(t) <= ord('Z'):
            if not ord('A') <= letter <= ord('Z'):
                letter -= 26
    else:
        letter = ord(t)

    return chr(letter)

def versleutel(zin, aantal):
    uitkomst = ''
    for t in zin:
        uitkomst += roteer_letter(t, aantal)

    return uitkomst
