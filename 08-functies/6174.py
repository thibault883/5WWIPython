def splits(getal):
    stap = 0
    for i in str(getal):
        stap += 1
        if stap == 1:
            getal_1 = int(i)
        elif stap == 2:
            getal_2 = int(i)
        elif stap == 3:
            getal_3 = int(i)
        else:
            getal_4 = int(i)

    return getal_1, getal_2, getal_3, getal_4

def oplopende_cijfers(a, b, c, d):
    hoogste = max(a, b, c, d)
    laagste = min(a, b, c, d)
    mid_1 = int(max(min(a, b), min(a, c), min(b, c)))
    mid_2 = a + b + c + d - hoogste - laagste - mid_1
    mid_laag = min(mid_1, mid_2)
    mid_hoog = max(mid_1, mid_2)
    return laagste, mid_laag, mid_hoog, hoogste

def op_af_getallen(a, b, c, d):
    cijfer_1 = str(a) + str(b) + str(c) + str(d)
    cijfer_2 = str(d) + str(c) + str(b) + str(a)

    return cijfer_1, cijfer_2

def verschil(a, b):
    verschil = int(a) - int(b)

    return str(verschil)

def kaprekar(getal):
    uitkomst = ''
    while getal != 6174:
        getal_1, getal_2, getal_3, getal_4 = splits(getal)
        laagste, mid_laag, mid_hoog, hoogste = oplopende_cijfers(getal_1, getal_2, getal_3, getal_4)
        cijfer_1, cijfer_2 = op_af_getallen(laagste, mid_laag, mid_hoog, hoogste)
        getal = int(verschil(cijfer_2, cijfer_1))
        uitkomst += '{} - {} = {}\n'.format(cijfer_2, cijfer_1, getal)

    return uitkomst.strip()

print(splits(1234))
