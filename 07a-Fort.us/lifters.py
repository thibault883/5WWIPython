aantal = int(input('hoeveel lifters: '))
hoogste = float(input('geef een score: '))
uitvoer = 0

for i in range(aantal - 1):
    score = float(input('geef een score: '))
    if i < ((aantal // 2) - 1):
        hoogste = max(score, hoogste)
    else:
        if hoogste < score:
            uitvoer = score
            hoogste = 1

if uitvoer == 0:
    uitvoer = score

print(uitvoer)

