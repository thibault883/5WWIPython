def dubbels(lijst):
    res = []

    for element in lijst:
        if lijst.count(element) > 1 and element not in res:
            res.append(element)

    return res

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))
