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
    mid_1 = int(max(min(getal_1, getal_2), min(getal_1, getal_3), min(getal_3, getal_2)))
    mid_2 = int(getal_3) + int(getal_2) + int(getal_1) + int(getal_4) - int(hoogste) - int(laagste) - int(mid_1)
    mid_laag = min(mid_1, mid_2)
    mid_hoog = max(mid_1, mid_2)
    return laagste, mid_laag, mid_hoog, hoogste

def op_af_getallen(laagste, mid_laag, mid_hoog, hoogste):
    cijfer_1 = str(laagste) + str(mid_laag) + str(mid_hoog) + str(hoogste)
    cijfer_2 = str(hoogste) + str(mid_hoog) + str(mid_laag) + str(laagste)

    return cijfer_1, cijfer_2

def verschil(cijfer_1, cijfer_2):
    verschil = int(cijfer_1) - int(cijfer_2)

    return verschil

def kaprekar(getal):
    while uitvoer != 6174:
        getal_1, getal_2, getal_3, getal_4 = splits(getal)
        laagste, mid_laag, mid_hoog, hoogste = oplopende_cijfers(getal_1, getal_2, getal_3, getal_4)
        cijfer_1, cijfer_2 = op_af_getallen(laagste, mid_laag, mid_hoog, hoogste)
        uitvoer = verschil(cijfer_2, cijfer_1)
        return uitvoer
        getal = uitvoer



def leuk(getal):
    uitvoer = ''
    while getal != 5:
        uitvoer += str(getal) + "\n"
        getal += 1
    return uitvoer


print(leuk(2))
