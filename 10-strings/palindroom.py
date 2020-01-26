def is_palindroom(woord):
    controle = 0
    for i in range(0, len(woord)):
        if woord[i] == woord[(-i - 1)]:
            controle += 1

    return controle == len(woord)



