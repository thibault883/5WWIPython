#seconde = int(input("geef de tijd: "))

#stap_voor, stapvoor_1, stap_achter, stapachter_1 = 0, 0, 0, 0

#for i in range(seconde):
    #if i % 2 == 0:
        #stap_voor = stap_voor + 2
        #stapvoor_1 += stap_voor
    #else:
        #stap_achter = stap_achter + 1
        #stapachter_1 += stap_achter

#print(stapvoor_1 - stapachter_1)

tijd = int(input('geef de tijd: '))
som = 0
for i in range(tijd):
    if i % 2 == 0:
        som += i + 2
    else:
        som -= (i + 1) / 2
print(round(som))
