def dubbels(lijst):
    uitvoer = []
    for i in range(len(lijst)):
        if lijst[i] not in uitvoer and lijst[i] in (lijst[:i] + lijst[i + 1:]):
            uitvoer += [lijst[i]]

    return uitvoer

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))
