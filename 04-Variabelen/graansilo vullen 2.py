#invoer
b = float(input("geef de breedte: "))
l = float(input("geef de lengte: "))
c = float(input("geef graan: "))
r = float(input("geef straal: "))
h = float(input("geef hoogte: "))
pi = 3.1415926535897931

#berekening
opp = l * b
v = r**2 * pi * h
aantal_graan = opp * c / 10000
aantal_cilos = aantal_graan // v
laatste_cilo = aantal_graan % v
h2 = laatste_cilo / (r**2 * pi)
aantal_cilos2 = int(aantal_cilos + 1)



#uitvoer
print(aantal_cilos2)
print(h2)
