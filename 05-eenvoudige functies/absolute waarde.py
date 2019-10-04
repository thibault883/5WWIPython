#invoer
eerste_getal = float(input("geef een random getal: "))
tweede_getal = float(input("geef een random getal: "))

#berekening
uitkomst_1 = abs(abs(eerste_getal)-abs(tweede_getal))
uitkomst_2 = abs(eerste_getal - tweede_getal)

#uitvoer
uitvoer = "{:.4f} \N{LESS-THAN OR EQUAL TO} {:.4f}"
print(uitvoer.format(uitkomst_1, uitkomst_2))

