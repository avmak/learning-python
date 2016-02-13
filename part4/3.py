# Функция сложения произвольного количества аргументов одного типа

def adder(*pargs):
	summ = pargs[0]													# выделение первого передаваемого аргумента переменной

	if type(summ) == type({}):										# если передаваемый аргумент словарь, то вывести сообщение и выйти из функции
		return print('This is a dictionary!!!')

	for i in pargs[1:]:												# если передаваемых аргументов больше одного, и их типы отличаются, вывести сообщение и выйти из функции
		if type(summ) != type(i):
			return print('The types of arguments are different!')
		
	for i in pargs[1:]:												# цикл сложения значений передаваемых аргументов
		summ += i
	print('Type arguments amount:', type(summ))
	return summ

# Тестирование функции

print(adder('py' 'th', 'on'))
print(adder(['p'], ['y'], ['t'], ['h'], ['o'], ['n']))
print(adder(3.14))
print(adder(600, 60, 6))
adder('py', 2, 3)
adder({1:2}, {2:3})
