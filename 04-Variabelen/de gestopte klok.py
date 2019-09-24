#invoer
uur1 = int(input("geef uur: "))
min1 = int(input("geef min: "))

uur2 = int(input("geef uur: "))
min2 = int(input("geef min: "))

uur3 = int(input("geef uur: "))
min3 = int(input("geef min: "))

uur4 = int(input("geef uur: "))
min4 = int(input("geef min: "))

#bereking
y1 = (uur1 * 60) + min1
y2 = (uur2 * 60) + min2
y3 = (uur3 * 60) + min3
y4 = (uur4 * 60) + min4
yy = y4 - y1
y0 = y3 - y2
vertrek = y4 - y1 + (720 - (720* (yy / abs(yy))))
yy5 = y3 - y2 + (720 - (720* (y0 / abs(y0))))
y5 = (vertrek - yy5) / 2
y6 = y3 + y5
y7 = y6 // 60
y8 = y6 % 60
raar = y7 - 24
y7 -= 12 + (12 * (raar/abs(raar)))

#uitvoer
print(int(y7))
print(int(y8))
