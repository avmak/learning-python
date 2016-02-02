L = [1, 2, 4, 8, 16, 32, 64]
n = 2 ** 5
 
if n in L:
    print('at index', L.index(n))
else:
    print(n, 'not found')