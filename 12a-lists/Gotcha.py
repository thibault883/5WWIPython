def ik_heb_gemoord(lijst, moordenaar):
    slachtoffer = lijst.index(moordenaar) + 1
    slachtoffer_2 = slachtoffer + 1
    while slachtoffer >= len(lijst):
        slachtoffer -= len(lijst)
    while slachtoffer_2 >= len(lijst):
        slachtoffer_2 -= len(lijst)
    if len(lijst) != 1:
        lijst.remove(lijst[slachtoffer])

    return lijst[slachtoffer_2], lijst

def ik_ben_vermoord(lijst, slachtoffer):
    volgend = lijst.index(slachtoffer) + 1
    while volgend >= len(lijst):
        volgend -= len(lijst)
    if len(lijst) != 1:
        lijst.remove(slachtoffer)

    return lijst[volgend], lijst

print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'piet'))
