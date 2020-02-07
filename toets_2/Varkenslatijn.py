def verwijder_medeklinkers(woord):
    a = 0
    for i in range(len(woord)):
        if woord[i] in 'aeoiu' and a != 1:
            uitkomst = woord[i:]
            a = 1

    return uitkomst

def varkenslatijn(woord):
    if woord[0] in 'aeoiu':
        woord += 'ibus'
    elif woord[-1] in 'aiu':
        woord += 'nt'
    else:
        woord = verwijder_medeklinkers(woord) + 'itum'

    woord = woord.replace('j', 'i')
    woord = woord.replace('z', '')
    woord = woord.replace('y', '')

    return woord

def vertaal(zin):
    uitkomst = ''
    zin = zin.split()
    for woord in zin:
        uitkomst += varkenslatijn(woord) + ' '

    return uitkomst[:-1]

print(varkenslatijn('paraplu'))
