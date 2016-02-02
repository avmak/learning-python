S = 'slipknot'
su = 0

for x in S:
    print(ord(x), end = ' ')
    su += ord(x)

print('\nThe amount of characters in the string =', su)