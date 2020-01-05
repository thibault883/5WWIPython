reeks = int(input("geef het nummer: "))
aantal,hoogste = 0,0

while reeks > 0:
    hoogste = max(reeks, hoogste)
    reeks = int(input("geef het nummer: "))
    aantal += 1

tanks = round((((aantal + 1) * hoogste) / (aantal)) - 1)
print("Het aantal geproduceerde tanks wordt geschat op " + str(tanks) + ".")
