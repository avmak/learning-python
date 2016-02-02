L = [1, 2, 4, 8, 16, 32, 64]
n = 2 ** 5
 
for x in L:
    if x == n:
        print('at index', L.index(x))
        break
else:
    print(n, 'not found')