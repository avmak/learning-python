L = []
n = 2 ** 5

for x in range(7):
    L.append(2 ** x)
 
if n in L:
    print('at index', L.index(n))
else:
    print(n, 'not found')