def countLines(name):													#Function counts the line in the file
	return len(open(name).readlines())

def countChars(name):													#Function counts the characters in the file
	return len(open(name).read())

def test(name):															#Test function
	return countLines(name), countChars(name)

#Option self-test modules
if __name__ == '__main__': print(test('myclient.py'))

#if __name__ == '__main__': print(test(input('Enter file name: ')))		#Using the user input

#if __name__ == '__main__':												#Using the command line arguments
#	import sys
#	print(test(sys.argv[1]))
