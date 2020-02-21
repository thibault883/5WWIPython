def ik_heb_gemoord(lijst, moordenaar):
    if len(lijst) != 1:
        lijst.remove(lijst[(lijst.index(moordenaar) + 1) % len(lijst)])

    return lijst[(lijst.index(moordenaar) + 1) % len(lijst)], lijst

def ik_ben_vermoord(lijst, slachtoffer):
    index = lijst.index(slachtoffer)
    if len(lijst) != 1:
        lijst.remove(slachtoffer)
    volgend = index % len(lijst)

    return lijst[volgend], lijst

print(ik_ben_vermoord(['jan', 'piet', 'korneel'],'piet'))
