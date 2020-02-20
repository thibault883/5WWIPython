invoer = input('geef iets: ')
queue, uitvoer = [], ''

while invoer != 'STOP':
    if invoer == '?':
        if len(queue) != 0:
            uitvoer += queue[0] + '\n'
            queue = queue[1:]
    else:
        queue += [str(invoer)]
    invoer = input('geef iets: ')

print(uitvoer.strip())

