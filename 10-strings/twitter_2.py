bericht = input('geef een bericht: ')
hashtag = bericht.find('#')
woorden = ''

while hashtag != -1:
    spatie = bericht[hashtag:].find(' ')
    woorden += bericht[hashtag + 1: hashtag + spatie] + '\n'

    bericht = bericht[hashtag + spatie + 1:]
    hashtag = bericht.find('#')

print(woorden[:len(woorden)-1])


