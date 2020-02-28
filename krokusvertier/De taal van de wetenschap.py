woord_1 = input('geef een woord: ')
woord_2 = input('geef een woord: ')
i, prefix, k, suffix = 0, '', 1, ''

while i < len(woord_2) and i < len(woord_1):
    if woord_1[i] == woord_2[i] and len(prefix) == i:
        prefix += woord_1[i]
    i += 1

while k < (len(woord_2) + 1) and k < (len(woord_1) + 1):
    if woord_1[-k] == woord_2[-k] and len(suffix) + 1 == k:
        suffix += woord_1[-k]
    k += 1
suffix = suffix[::-1]

if len(suffix) != 0:
    stam_1 = woord_1[len(prefix):-len(suffix)]
    stam_2 = woord_2[len(prefix):-len(suffix)]
else:
    stam_1 = woord_1[len(prefix):]
    stam_2 = woord_2[len(prefix):]

if len(stam_1) > len(stam_2):
    aantal = len(stam_1)
else:
    aantal = len(stam_2)

print('{}┏{:^{}}┓'.format(' ' * len(prefix), stam_1, aantal))
print('{}┫{}┣{}'.format(prefix, ' ' * aantal, suffix))
print('{}┗{:^{}}┛'.format(' ' * len(prefix), stam_2, aantal))
