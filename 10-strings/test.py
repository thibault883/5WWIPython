woord = input('woord: ')

for i in range(0, len(woord)):
    if woord[i] in 'aeoui':
        woord = woord[:i] + '*' + woord[i + 1:]

print(woord)

# rtfm = read the fucking manule
