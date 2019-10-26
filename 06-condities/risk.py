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
