geld = float(input('geef het geld: '))

rsz = round(geld * (13.07/100), 2)
geld -= rsz
schijf_1 = 0
schijf_2 = 0
schijf_3 = 0
schijf_4 = 0

if geld - 13250.00 >= 0:
    schijf_1 = 13250.00 - 8860.00
    geld_over = geld - 13250.00
    if geld_over - 10140.00 >= 0:
        schijf_2 = 10140.00
        geld_over -= 10140.00
        if geld_over - 17090.00 >= 0:
            schijf_3 = 17090.00
            schijf_4 = geld_over - 17090.00
        else:
            schijf_3 = geld_over
    else:
        schijf_2 = geld_over
else:
    if geld - 8860.00 <= 0:
        schijf_1 = 0
    else:
        schijf_1 = geld - 8860.00

verheffing = (schijf_1 * (1/4)) + (schijf_2 * (4/10)) + (schijf_3 * (45/100)) + (schijf_4 * (1/2))

netto_jaarsalaris = round(geld - verheffing, 2)
netto_maandsalaris = netto_jaarsalaris / 12


print('+ bruto jaarsalaris   {:.2f}'.format(geld))
print('- rsz                  {:.2f}'.format(rsz))
print('- voorheffing          {:.2f}'.format(verheffing))
print('==============================')
print('+ netto jaarsalaris   {:.2f}'.format(netto_jaarsalaris))
print('+ netto maandsalaris   {:.2f}'.format(netto_maandsalaris))
