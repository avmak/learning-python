# Функция копирования словаря

def copyDict(sDict):
	newD = {}
	for i in list(sDict.keys()):
		newD[i] = sDict[i]
	return newD
