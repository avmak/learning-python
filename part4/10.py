# Файл timeseqs.py для тестирования различный вариантов нахождения квадратного корня

import sys, math, mytimer2
reps = 1000
repslist = range(reps)

def forLoop1():
	res = []
	for x in repslist:
		res.append(math.sqrt(x))
	return res

def forLoop2():
	res = []
	for x in repslist:
		res.append(x ** .5)
	return res

def forLoop3():
	res = []
	for x in repslist:
		res.append(pow(x, .5))
	return res

def listComp1():
	return [math.sqrt(x) for x in repslist]

def listComp2():
	return [x ** .5 for x in repslist]

def listComp3():
	return [pow(x, .5) for x in repslist]

def mapCall1():
	return list(map((lambda x: math.sqrt(x)), repslist))

def mapCall2():
	return list(map((lambda x: x ** .5), repslist))

def mapCall3():
	return list(map((lambda x: pow(x, .5)), repslist))

def genExpr1():
	return list(math.sqrt(x) for x in repslist)

def genExpr2():
	return list(x ** .5 for x in repslist)

def genExpr3():
	return list(pow(x, .5) for x in repslist)

def genFunc1():
	def gen():
		for x in repslist:
			yield math.sqrt(x)
	return list(gen())

def genFunc2():
	def gen():
		for x in repslist:
			yield x ** .5
	return list(gen())

def genFunc3():
	def gen():
		for x in repslist:
			yield pow(x, .5)
	return list(gen())

print(sys.version)
for tester in (mytimer2.timer, mytimer2.best):
	print('<{0}>'.format(tester.__name__))
	for test in (forLoop1, forLoop2, forLoop3, listComp1, listComp2,
				 listComp3, mapCall1, mapCall2, mapCall3, genExpr1, genExpr2,
				 genExpr3, genFunc1, genFunc2, genFunc3):
		elapsed, result = tester(test)
		print('-' * 33)
		print('{0:<9}: {1:.5f}'.format(test.__name__, elapsed))
