#
#16.1
#In een rechthoekige driehoek met rechthoekszijden a = 92.07 en b = 16.10 is de schuine zijde 93.47

from math import sqrt

#invoer
a = float(input('lengte zijde a: '))
b = float(input('lengte zijde b: '))

#berekening
c = round(sqrt(pow(a, 2) + pow(b, 2)), 2)
a = round(a, 2)
b = round(b, 2)
#uitvoer
uitvoer = 'In een rechthoekige driehoek met rechthoekszijden a = {} en b = {} is de schuine zijde {}'
print(uitvoer.format(a, b, c))
