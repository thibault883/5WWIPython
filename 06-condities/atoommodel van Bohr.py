#invoer
ant_e = int(input('geef het aantal elektronen: '))

#berekening
if ant_e > 124:
    print('De Q-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')
elif ant_e > 92:
    print('De P-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')
elif ant_e > 60:
    print('De O-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')
elif ant_e > 28:
    print('De N-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')
elif ant_e > 10:
    print('De M-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')
elif ant_e > 2:
    print('De L-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')
else:
    print('De K-schil is de buitenste schil van een stabiel atoom met', ant_e,'elektronen.')

