def dubbels(lijst):
    uitvoer = []
    for i in range(len(lijst)):
        if lijst[i] not in uitvoer and lijst[i] in (lijst[:i] + lijst[i + 1:]):
            uitvoer.append(lijst[i])

    return uitvoer


