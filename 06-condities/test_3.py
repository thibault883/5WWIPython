getal_1 = 4
getal_2 = 3
getal_3 = 7
getal_4 = 10

hoogste = max(getal_4, getal_3, getal_2, getal_1)
laagste = min(getal_4, getal_3, getal_2, getal_1)
mid_1 = max(min(getal_1,getal_2),min(getal_1,getal_3),min(getal_3,getal_2))
mid_2 = getal_3 + getal_2 + getal_1 + getal_4 - hoogste - laagste - mid_1

print(hoogste, mid_1, mid_2, laagste)
