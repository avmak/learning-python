L = [1, 2, 4, 8, 16, 32, 64]
n = 2 ** 5
i = 0
 
while i < len(L):
    if n == L[i]:
        print('at index', i)
        break
    else:
        i += 1
else:
    print(n, 'not found')
