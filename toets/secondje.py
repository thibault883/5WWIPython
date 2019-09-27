#invoer
sec = int(input("geef aantal seconden: "))

#berekening
dagen = sec // 86400
sec %= 86400

uren = sec // 3600
sec %= 3600

min = sec // 60
sec %= 60

#uitvoer
print(str(dagen) + "d " + str(uren) + ":" + str(min) + ":" + str(sec))
