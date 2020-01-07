tijd = int(input('geef de tijd: '))
som = 0
for i in range(tijd):
    if i % 2 == 0:
        som += i + 2
    else:
        som -= (i + 1) / 2
print(round(som))
