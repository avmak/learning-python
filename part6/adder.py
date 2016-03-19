class Adder:
	def __init__(self, datain):
		self.data = datain
	def __add__(self, other):
		print('addition is executed')
		return self.add(other)		
	def add(self, x, y):
		print("Not Implemented")

class ListAdder(Adder):
	def add(self, x):
		return self.data + x

class DictAdder(Adder):
	def add(self, x):
		adddict = {}
		for i in self.data.keys():
			adddict[i] = self.data[i]
		for i in x.keys():
			adddict[i] = x[i]
		return adddict
