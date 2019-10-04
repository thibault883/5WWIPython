#18 + 20     = 38
#   180 + 200    = 380
# 1800 + 2000   = 3800
#18000 + 20000  = 38000
#180000 + 200000 = 380000
#invoer
a = int(input('geef een cijfer tussen 0 en 20: '))
b = int(input('geef een cijfer tussen 0 en 20: '))

#berekening
uitkomst = int(a + b)


#uitvoer
uitvoer = '{:6d} + {:<6d} = {:d}'
print(uitvoer.format(a, b, uitkomst))
print(uitvoer.format(a * 10, b * 10, uitkomst * 10))
print(uitvoer.format(a * pow(10, 2), b * pow(10, 2), uitkomst * pow(10, 2)))
print(uitvoer.format(a * pow(10, 3), b * pow(10, 3), uitkomst * pow(10, 3)))
print(uitvoer.format(a * pow(10, 4), b * pow(10, 4), uitkomst * pow(10, 4)))
