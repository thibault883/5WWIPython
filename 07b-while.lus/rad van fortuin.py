woord = input('geef een woord: ')
geld = int(input('geef geld: '))
letter = input('geef de letter: ')
totaal = 0
vorige_letter = ''
while letter in woord and vorige_letter != letter :
    vorige_letter = letter
    totaal += geld
    letter = input('geef de letter: ')


print(totaal)
