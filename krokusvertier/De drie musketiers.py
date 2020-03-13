aantal = int(input())
tekst = []
for i in range(aantal):
    regel = input()
    tekst.append(regel)
for k in range(len(tekst)):
    for m in range(len(tekst[k])):
        if (tekst[k][m - 1] == tekst[k][m + 1] and tekst[k][m - 1] == tekst[k - 1][m]) or (tekst[k][m - 1] == tekst[k][m + 1] and tekst[k][m - 1] == tekst[k + 1][m])

