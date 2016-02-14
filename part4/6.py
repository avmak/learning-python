# Функция объединения двух словарей

def addDict(sDict1, sDict2):
	if type(sDict1) == type([]):
		return sDict1 + sDict2
	else:
		sumD = {}
		for i in list(sDict1.keys()) + list(sDict2.keys()):
			if i in sDict1.keys():
				sumD[i] = sDict1[i]
			else:
				sumD[i] = sDict2[i]
		return sumD


D1 = {'a': 1, 'b': 2, 'c': 3}
D2 = {'c': 4, 'd': 5, 'e': 6}
print(addDict(D1, D2))

L1 = ['Spit', 'It']
L2 = ['Out']
print(addDict(L1, L2))
