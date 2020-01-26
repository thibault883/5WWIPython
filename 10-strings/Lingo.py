def hint(geraden, woord):
    hint = ''
    for i in range(0, len(woord)):
        if geraden[i] in woord:
            if geraden[i] == woord[i]:
                hint += geraden[i].upper()
            else:
                hint += geraden[i]
        else:
            hint += '.'

    return hint

print(hint('amorf', 'kiste'))
