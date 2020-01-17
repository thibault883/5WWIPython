from random import randint

def gooi_muntstuk():
    muntstuk = 'munt'
    if not randint(0,2):
        muntstuk = 'kop'
    return muntstuk

for i in range(10):
    print(gooi_muntstuk())
#print(rg, muntstuk)
