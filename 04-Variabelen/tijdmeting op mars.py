#invoer
sol_days = y = int(input('geef het aantal soldagen: '))
sol_seconden = 88775.244

#berekening
sol = sol_days * sol_seconden

sol1 = int(sol // (24 * 60 * 60 ))
sol = sol % (24 * 60 *60)

sol2 = int(sol // (60 * 60))
sol = sol % (60 *60)

sol3 = int(sol // 60)
sol = sol % 60

sol4 = int(sol)

#uivoer
print(str(y),'sol =',sol1,'dagen,',sol2,'uren,',sol3,'minuten en',sol4,'seconden')
