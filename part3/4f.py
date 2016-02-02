L = list(map(lambda x: 2 ** x, range(7)))
n = 2 ** 5
 
if n in L:
    print('at index', L.index(n))
else:
    print(n, 'not found')