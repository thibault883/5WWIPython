from operator import itemgetter

def fruitstuk_toevoegen(fruitmand, fruit):
    uitkomst, uitvoer = [], []
    for i in range(len(fruitmand)):
        if len(fruitmand[i]) != len(fruit):
            uitkomst += [[fruitmand[i], len(fruitmand[i])]]
    uitkomst.append([fruit, len(fruit)])
    uitkomst.sort(key=itemgetter(1))
    for k in range(len(uitkomst)):
        uitvoer += [uitkomst[k][0]]

    return uitvoer

def maak_fruitmand(mand):
    nieuwe_mand = [mand[0]]
    for i in range(1, len(mand)):
        nieuwe_mand = fruitstuk_toevoegen(nieuwe_mand, mand[i])

    return nieuwe_mand

print(maak_fruitmand(['kiwi', 'peer', 'kiwi', 'peer', 'kiwi']))
