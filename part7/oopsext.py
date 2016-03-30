class MyError(Exception): pass

def oops():
	raise MyError('Error!!!')

def ux():
	try:
		oops()
	except (IndexError, MyError):
		import sys
		ch = '....'
		print('exc caight!\n', ch, sys.exc_info()[0], sys.exc_info()[1])
	else:
		print("exc don't caught!")

if __name__ == '__main__':
	ux()
