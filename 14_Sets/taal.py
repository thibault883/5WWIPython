def behoort_tot_taal(woord, letters):
    woord = set(woord.replace(' ', ''))
    if len(woord) == 0:
        woord = 'false'

    return letters.issuperset(woord)

def is_onleesbaar(woord, letters):
    return len(letters.intersection(woord)) == 0

def perfect_woord(woord, letters):
    return letters.issubset(woord)


print(behoort_tot_taal('',{'e', 'l', 'h', 'r', 'o', 'w', 'd'}))
