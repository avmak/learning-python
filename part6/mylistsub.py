from mylist import MyList

class MyListSub(MyList):
	count = 0
	def __init__(self, listin = []):
		self.countadd = 0
		MyList.__init__(self, listin)

	def __add__(self, otherlist):
		self.countadd += 1
		MyListSub.count += 1
		self.outcount()
		if isinstance(otherlist, MyListSub):
			otherlist = otherlist.data
		return MyListSub(MyList.__add__(self, otherlist))

	def outcount(self):
		print("Counter additions: ", self.countadd)
		print("Counter initialization", MyListSub.count)

if __name__ == '__main__':
	x = MyListSub('abc')
	y = MyListSub('def')
	print(x + ['de'])
	print(x + ['def'])
	print(y + ['h'])
	print(x + y)
