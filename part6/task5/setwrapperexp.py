from setwrapper import Set

class expSet(Set):
	def intersect(self, *other):
		res = []
		for x in self.data:
			for seq in other:
				if x not in seq: break
			else:
				res.append(x)
		return Set(res)

	def union(self, *other):
		res = self.data[:]
		for seq in other:
			for x in seq:
				if not x in res:
					res.append(x)
		return Set(res)
