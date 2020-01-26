tweet = input('geef een tweet: ')

for i in range(0, len(tweet)):
    woord = ''
    if tweet[i] == '#':
        while tweet[i] != ' ':
            woord += tweet[i]
            i += 1
        woord = woord[1:]
        print(woord)
