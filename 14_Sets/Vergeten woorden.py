def vergeten_woorden(tekst, woorden):
    wel = 0
    woorden = list(woorden)
    for i in woorden:
        if i in tekst:
            wel += 1

    return len(woorden), len(woorden) - wel, wel

print(vergeten_woorden('i love databases and sql',{'python', 'world', 'hello', 'java'}))

