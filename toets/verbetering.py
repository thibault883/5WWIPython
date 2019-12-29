dag = int(input('geef de dag: '))
maand = int(input('geef de maand: '))
jaar = int(input('geef het jaar: '))

dag += 1

if maand == 2:
    if (jaar % 100 == 0 and jaar % 400 != 0) or jaar % 4 != 0:
        if dag == 29:
            dag = 1
            maand += 1
    else:
        if dag == 30:
            dag = 1
            maand += 1
else:
    if maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10:
        if dag == 32:
            dag = 1
            maand += 1
    elif maand == 12:
        if dag == 32:
            dag = 1
            maand = 1
            jaar += 1
    else:
        if dag == 31:
            dag = 1
            maand += 1

print(str(dag) + '/' + str(maand) + '/' + str(jaar))

#===================================================

