from math import sin, cos, pi
getal = input('geef een getal: ')
x, y = 0, 0

for i in getal:
    if i != '.':
        x += cos((pi / 2) - (int(i) * 0.2 * pi))
        y += sin((pi / 2) - (int(i) * 0.2 * pi))

print('Getal {} wandelt naar positie ({:.2f}, {:.2f}).'.format(getal, x, y))

