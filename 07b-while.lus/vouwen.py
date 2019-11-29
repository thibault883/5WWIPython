dikte = int(input('geef de dikte: '))
afstand = int(input('geef de afstand: '))
vouwen = 0
while dikte < afstand:
    dikte *= 2
    vouwen += 1

print('Na', vouwen ,'keer vouwen bedraagt de dikte van het papier', 549755813888,'mm.')

