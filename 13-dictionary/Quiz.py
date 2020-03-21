def verlaat_ploeg(naam, ploeg, ingeschreven):
    ingeschreven[ploeg].pop(ingeschreven[ploeg].index(naam))
    if len(ingeschreven[ploeg]) == 0:
        ingeschreven.pop(ploeg)

    return ingeschreven

def vervoegt_ploeg(naam, ploeg, ingeschreven):
    if ploeg in ingeschreven:
        ingeschreven[ploeg].append(naam)
    else:
        ingeschreven[ploeg] = [naam]

    return ingeschreven

print(vervoegt_ploeg('Els','Sinbox',{'Sinbox': ['An', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))
