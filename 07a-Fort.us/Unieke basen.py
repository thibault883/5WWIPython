aantal = int(input('geef het aantal keer: '))
dna_1, dna_2, dna_3, dna_4 = '', '', '', ''
verschillende = 0
for i in range(aantal):
    soort = input('geef de soort: ')
    if soort == 'A':
        dna_1 = ' A'
    elif soort == 'T':
        dna_2 = ' T'
    elif soort == 'G':
        dna_3 = ' G'
    elif soort == 'C':
        dna_4 = ' C'
verschillende = int((len(str(dna_1 + dna_2 + dna_3 + dna_4))) / 2)
if verschillende == 1 or verschillende == 0:
    print('De DNA-keting bevat', verschillende ,'soort base:' + dna_1 + dna_4 + dna_3 + dna_2)
else:
    print('De DNA-keting bevat', verschillende ,'verschillende soorten basen:' + dna_1 + dna_4 + dna_3 + dna_2)


