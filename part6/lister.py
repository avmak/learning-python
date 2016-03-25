class ListInstance:
	def __str__(self):
		return '<Instance of %s, superclasses = [%s], address %s:\n%s>' % (
							self.__class__.__name__,
							self._superclasses(),
							id(self),
							self.__attrnames())
	
	def __attrnames(self):
		result = ''
		for attr in sorted(self.__dict__):
			result += '\tname %s = %s\n' % (attr, self.__dict__[attr])
		return result

	def _superclasses(self):
		supcl = []
		for obj in self.__class__.__bases__:
			supcl.append(obj.__name__)
		return ', '.join(supcl)
