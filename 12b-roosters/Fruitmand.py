def fruitstuk_toevoegen(fruitmand, fruit):
    for i in range(len(fruitmand)):
        if len(fruitmand[i]) == len(fruit):
            fruitmand.pop(i)
    fruitmand.append(fruit)
    aantal, uitvoer = len(fruitmand), []
    for k in range(aantal):
        hoogste = 0
        for m in range(len(fruitmand)):
            hoogste = max(hoogste, len(fruitmand[m]))
            if hoogste == len(fruitmand[m]):
                weg = m
        uitvoer += [fruitmand[weg]]
        fruitmand.pop(weg)

    return uitvoer[::-1]

