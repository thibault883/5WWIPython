def is_palindroom(woord):
    uitkomst = 'True'
    for i in range(len(woord)):
        if woord[i] != woord[(-i - 1)]:
            uitkomst = 'False'

    return uitkomst

print(is_palindroom('tarwerat'))
