def splits(getal):
    stap = 0
    for i in str(getal):
        stap += 1
        if stap == 1:
            getal_1 = i
        elif stap == 2:
            getal_2 = i
        elif stap == 3:
            getal_3 = i
        else:
            getal_4 = i

    return getal_1, getal_2, getal_3, getal_4

def oplopende_cijfers(getal_1, getal_2, getal_3, getal_4):
    hoogste = max(getal_1, getal_2, getal_3, getal_4)
    laagste = min(getal_1, getal_2, getal_3, getal_4)
    mid_1 = max(min(getal_1, getal_2), min(getal_1, getal_3), min(getal_3, getal_2))
    mid_2 = getal_3 + getal_2 + getal_1 + getal_4 - hoogste - laagste - mid_1

    return laagste, min(mid_1, mid_2), max(mid_1, mid_2), hoogste

def op_af_getallen(laagste, mid_1, mid_2, hoogste):
    cijfer_1 = str(laagste) + str(mid_1) + str(mid_2) + str(hoogste)
    cijfer_2 = str(hoogste) + str(mid_2) + str(mid_1) + str(laagste)

    return cijfer_1, cijfer_2

def verschil(cijfer_1, cijfer_2):
    verschil = int(cijfer_1) - int(cijfer_2)

    return verschil

def kaprekar(getal):
    while uitvoer != int(6174):
        uitvoer = verschil(oplopende_cijfers(splits(getal)))
        return (str(max(oplopende_cijfers(splits(getal)))) + ' - ' + (str(min(oplopende_cijfers(splits(getal)))) + ' = ' + str(uitvoer)
        getal = 0
        getal += uitvoer

print(kaprekar(5342))





