def dagprijs(lijst):
    som, k = 0, 1
    for i in range(len(lijst) // 2):
        if lijst[k - 1] == 'middagmaal':
            som += (5.3 * lijst[k])
        elif lijst[k - 1] == 'soep':
            som += (1.7 * lijst[k])
        else:
            som += (2.3 * lijst[k])
        k += 2

    return som

def weekprijs(lijst):
    week_som = 0
    for i in range(len(lijst)):
        week_som += dagprijs(lijst[i])

    return week_som

print(weekprijs((('middagmaal', 2, 'soep', 2, 'vieruurtje', 2), ('middagmaal', 1, 'soep', 1), ('soep', 3, 'vieruurtje', 3), ('middagmaal', 3, 'soep', 1), ('middagmaal', 3, 'soep', 3, 'vieruurtje', 1))))
