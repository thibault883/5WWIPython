for getal in range(2, 100):
    i = 2
    while getal % i != 0 and i != getal:
        i += 1
        if i == getal:
            print(getal)

