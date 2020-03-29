def boot_overlappend(boot, schepen):
    return not schepen.isdisjoint(boot)

def boot_toevoegen(boot, schepen):
    uitkomst = schepen
    if boot_overlappend(boot, schepen) == False:
        uitkomst = schepen.union(boot)

    return uitkomst

def vuur(coord, schepen):
    aantal = len(schepen)
    schepen.discard(coord)
    return aantal != len(schepen), schepen

print(vuur('I7',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))
