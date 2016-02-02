D = {'a':'s', 'b':'l', 'c':'i', 'd':'p', 'e':'k', 'f':'n', 'g':'o', 'h':'t'}

L = list(D.keys())
L.sort()

for x in L:
    print(x, '=>', D[x])