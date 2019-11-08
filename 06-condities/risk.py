#invoer
aanv_1 = int(input('geef het aantal ogen van de dobbelsteen: '))
aanv_2 = int(input('geef het aantal ogen van de dobbelsteen: '))
aanv_3 = int(input('geef het aantal ogen van de dobbelsteen: '))
verd_1 = int(input('geef het aantal ogen van de dobbelsteen: '))
verd_2 = int(input('geef het aantal ogen van de dobbelsteen: '))
verlies_aanv = 0
verlies_verd = 0

#berekening
eerste_aanv = max(aanv_2,aanv_1,aanv_3)
derde_aanv = min(aanv_2,aanv_1,aanv_3)
tweede_aanv = aanv_3 + aanv_2 + aanv_1 - eerste_aanv - derde_aanv

eerste_verd = max(verd_2,verd_1)
tweede_verd = min(verd_2,verd_1)

if eerste_aanv != eerste_verd:
    if eerste_aanv > eerste_verd:
        verlies_verd += 1
    else:
        verlies_aanv += 1
else:
    verlies_aanv += 1

if tweede_aanv != tweede_verd:
    if tweede_aanv > tweede_verd:
        verlies_verd += 1
    else:
        verlies_aanv += 1
else:
    verlies_aanv +=1

if verlies_aanv == 1:
    leg_1 = 'leger'
else:
    leg_1 = 'legers'

if verlies_verd == 1:
    leg_2 = 'leger'
else:
    leg_2 = 'legers'

print('aanvaller verliest', verlies_aanv , leg_1 +', verdediger verliest', verlies_verd, leg_2)

#middelste van 3 getallen
#max(min(a1, a2), min(a2, a3), min (a1, a3))

#middelste van 4 getallen
#mid_1 = max(min(x1, x2), min(x1, x3), min(x3, x2))
#mid_2 = x1 + x2 + x3 + x4 - max - min - mid_1
#print(max, max(mid_1,mid_2), min(mid_1,mid_2), min)
