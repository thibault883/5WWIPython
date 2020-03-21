def synoniemen(tekst, dic):
    uitkomst = ''
    woorden = tekst.split()
    for i in range(len(woorden)):
        if woorden[i] in dic:
            uitkomst += dic[woorden[i]] + ' '
        else:
            uitkomst += woorden[i] + ' '

    return uitkomst.strip()

print(synoniemen('knoeien levert stoute leerlingen een straf op',{'straf': 'sanctie', 'stout': 'kwaadaardig', 'leerling': 'cursist', 'leraar': 'docent', 'school': 'troep', 'knoeien': 'broddelen', 'kwaad': 'gebelgd', 'slecht': 'beroerd'}))
