def safe(func, *args):
	try:
		func(*args)
	except:
		import sys, traceback
		print('caught exception: ', sys.exc_info()[0])
		log = open(r'C:\traceback.txt', 'a')
		traceback.print_exc(file = log)
	else:
		print("didn't catch exception")
	finally:
		log.close()

if __name__ == '__main__':
	class MyError(Exception): pass

	def oops():
		raise MyError('Error!!!')

	safe(oops)
