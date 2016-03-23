class MyList:
	def __init__(self, listin = []):
		print("__init__ is performed")
		self.data = []
		if isinstance(listin, MyList):
			listin = listin.data[:]
		for x in listin:
			self.data.append(x)
	
	def __add__(self, otherlist):
		print("__add__ is performed")
		if isinstance(otherlist, MyList):
			otherlist = otherlist.data
		return MyList(self.data + otherlist)
	def __radd__(self, otherlist):
		print("__radd__ is performed")
		return MyList(otherlist + self.data)
	def __iadd__(self, otherlist):
		print("__iadd__ is performed")
		self.data += otherlist
		return self
	
	def __getitem__(self, index):
		print("get item: ", index)
		return self.data[index]

	def __iter__(self):
		print("__iter__ is performed")
		self.ix = 0
		return self
	def __next__(self):
		if self.ix == len(self.data):
			raise StopIteration
		item = self.data[self.ix]
		self.ix += 1
		return item

	def __len__(self):
		print("__len__ is performed")
		return len(self.data)

	def append(self, val):
		print("append is performed")
		self.data.append(val)

	def sort(self):
		print("sort is performed")
		self.data.sort()

	def __getattr__(self, nameattr):
		print("__getattr__ is performed")
		return getattr(self.data, nameattr)

	def __repr__(self):
		print("__repr__ is performed")
		return repr(self.data)

if __name__ == "__main__":
	x = MyList('123')
	y = MyList(x)
	print(y)
	print(y[2])
	print(y[0:2])
	print(y + ['2'])
	print(['2'] + y)
	print(x + y)
	y += ['2']
	print(y)
	for ix in y:
		print(ix, end = ' ')
	y.append('2')
	print(y)
	y.sort()
	print(y)
	y.reverse()
	print(y)
