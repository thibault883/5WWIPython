def roteer(woord, letter):
    while letter >= len(woord):
        letter -= len(woord)

    return woord[letter:] + woord[:letter]

print(roteer('asimov', 15))


