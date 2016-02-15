# Создание списка квадратных корней разными способами

import math

L = [2, 4, 9, 16, 25]

newL = []
for i in L:
	newL.append(math.sqrt(i))

list(map(math.sqrt, L))

[math.sqrt(i) for i in L]
