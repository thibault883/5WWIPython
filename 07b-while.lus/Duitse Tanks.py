reeks = int(input("geef het nummer: "))
aantal,hoogste = 0,0

while reeks > 0:
    reeks = int(input("geef het nummer: "))
    aantal += 1
    hoogste = max(reeks, hoogste)

