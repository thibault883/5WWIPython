#invoer
tjirps_minuut = int(input("geef het aantal tjirps per minuut: "))

#berekening
graden_F = 50 + ((tjirps_minuut - 40) / 4)
graden_C = 10 + ((tjirps_minuut - 40) / 7)

#uitvoer
print("temperatuur (Fahrenheit):", graden_F)
print("temperatuur (Celsius):", graden_C)
