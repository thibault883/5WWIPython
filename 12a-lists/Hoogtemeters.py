def hoogtemeters(lijst):
    uitvoer = []
    for i in range(len(lijst) - 1):
        uitvoer.append([lijst[i + 1] - lijst[i]])

    return uitvoer

def dalen_en_stijgen(lijst):
    dalen, stijgen = 0, 0
    for i in range(len(lijst)):
        if lijst[i] > 0:
            stijgen += lijst[i]
        else:
            dalen += (-lijst[i])

    return dalen, stijgen

print(dalen_en_stijgen([-761, 286, -113, 649, -547]))
