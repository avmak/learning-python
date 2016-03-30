def oops():
	#raise IndexError
	raise KeyError

def ux():
	try:
		oops()
	except IndexError:
		print('exc caight!')
	else:
		print("exc don't caught")

ux()
