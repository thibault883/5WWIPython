def printbaar_rek(lijst):
    uitkomst = ''
    for i in range(len(lijst)):
        for k in range(len(lijst[i])):
            uitkomst += lijst[-i - 1][k]
        uitkomst += '\n'

    return uitkomst.strip()

def speel(kleur, plaats, lijst):
    k = 'ok'
    for i in range(len(lijst)):
        if lijst[i][plaats] == 'O' and k != 'genoeg':
            lijst[i].pop(plaats)
            lijst[i].insert(plaats, kleur)
            k = 'genoeg'

    return lijst

print(speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))



