lijsten = int(input('hoeveel keer: '))
uitkomst = ''
for i in range(lijsten):
    hoogste, laagste= 0, 1000
    aantal = int(input('hoeveel in lijst: '))
    for k in range(aantal):
        cijfer = int(input('geef een cijfer: '))
        hoogste = max(cijfer, hoogste)
        laagste = min(cijfer, laagste)
    uitkomst += '{} {} {}\n'.format(i + 1, laagste, hoogste)

print(uitkomst)
