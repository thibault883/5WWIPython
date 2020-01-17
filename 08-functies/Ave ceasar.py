def is_letter(t):
    return ord('a') <= ord(t) <= ord('z') or ord('A') <= ord(t) <= ord('Z')

def roteer_letter(t, aantal):
    if is_letter(t) == 'True':
        letter = ord(t) + aantal
        if ord('a') <= letter <= ord('z') or ord('A') <= letter <= ord('Z'):
            chr(letter)
        else:
            if ord('a') <= ord(t) <= ord('z'):
                letter = letter - ord(t) + 96
            else ord('A') <= ord(t) <= ord('Z'):
                letter = letter - ord(t) + 64

