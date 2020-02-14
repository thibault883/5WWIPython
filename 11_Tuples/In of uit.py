def binnen_of_buiten(middelpunt, cirkel, punt):
    from math import sqrt
    afstand_cirkel = sqrt(pow(middelpunt[0] - cirkel[0], 2) + pow(middelpunt[1] - cirkel[1], 2))
    afstand_punt = sqrt(pow(middelpunt[0] - punt[0], 2) + pow(middelpunt[1] - punt[1], 2))
    if afstand_cirkel > afstand_punt:
        uitvoer = 'binnen'
    elif afstand_cirkel == afstand_punt:
        uitvoer = 'op'
    else:
        uitvoer = 'buiten'

    return uitvoer, round(afstand_punt, 4)


print(binnen_of_buiten((17, 31),(-10, 6),(-6, 26)))
