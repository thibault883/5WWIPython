def woord_frequentie(tekst):
    uitkomst = {}
    woorden = tekst.lower().replace('.', '').split()
    for i in range(len(woorden)):
        if woorden[i] not in uitkomst:
            uitkomst[woorden[i]] = 1
        else:
            uitkomst[woorden[i]] += 1

    return uitkomst

def woorden_per_frequentie(tekst):
    uitkomst = {}
    aantal = woord_frequentie(tekst)
    for key in aantal.keys():
        if aantal[key] in uitkomst:
            uitkomst[aantal[key]] += [key]
        else:
            uitkomst[aantal[key]] = [key]

    return uitkomst

def  meest_gebruikte_woorden(tekst):
    woorden = woorden_per_frequentie(tekst)
    hoogste = max(woorden.keys())

    return woorden[hoogste]


print(meest_gebruikte_woorden('Dit is een zin. En nog een zin. En een laatste zin.'))
