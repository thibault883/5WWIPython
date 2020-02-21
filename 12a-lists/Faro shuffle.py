def nieuw_kaartspel(kaarten, nummer):
    nieuw_kaart = []
    for i in range(len(kaarten)):
        k = 0
        while k < len(nummer):
            nieuw_kaart += [kaarten[i] + str(nummer[k])]
            k += 1

    return nieuw_kaart

def splits_kaartspel(lijst):
    uitvoer = (lijst[:(len(lijst) // 2)], lijst[(len(lijst) // 2):])

    return uitvoer

def faro_shuffle(kaarten_1, kaarten_2):
    uitvoer = []
    if len(kaarten_1) == len(kaarten_2):
        for i in range(len(kaarten_1)):
            uitvoer.append(kaarten_1[i])
            uitvoer.append(kaarten_2[i])

    return uitvoer

print(faro_shuffle(['dood 0', 'dood 1', 'liefde 0'],['liefde 1', 'tijd 0', 'tijd 1']))




