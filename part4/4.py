# функция сложения/конкатенации трех аргументов

def adder(good = 'py', bad = 'th', ugly = 'on'):
	return good + bad + ugly

print(adder())
print(adder('be'))
print(adder('be', 'tt'))
print(adder('be', 'tt', 'er'))
print(adder(ugly = 'er', good = 'be'))
print(adder(ugly = 'er', good = 'be', bad = 'tt'))

# функция сложения произвольного количества именованных аргументов

def adder1(**nargs):
	L = sorted(list(nargs.keys()))
	sum = nargs[L[0]]
	for i in L[1:]:
		sum += nargs[i]
	return sum

print(adder1(a = 1, b = 2, c = 3))
print(adder1(a = 'In', b = ' ', c = 'Flames'))
print(adder1(a = ['S', 'l'], b = ['i', 'p'], c = ['k', 'n'], d = ['o', 't']))
