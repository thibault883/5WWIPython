def fruitmand_maken(fruitmand):
    uitkomst = {}
    for i in range(len(fruitmand)):
        uitkomst[len(fruitmand[i])] = fruitmand[i]

    return uitkomst

def fruitmand_inpakken(fruitmand):
    uitkomst, i = [], 0
    while len(uitkomst) != len(fruitmand):
        if i in fruitmand:
            uitkomst.append(fruitmand[i])
        i += 1

    return uitkomst

print(fruitmand_inpakken({6: 'banaan', 7: 'aardbei', 4: 'peer', 5: 'appel', 3: 'bes', 11: 'sinaasappel', 8: 'framboos'}))
