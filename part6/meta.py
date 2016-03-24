class Meta:
	def __getattr__(self, attrname):
		print(attrname, "attribute is not specified")
	def __setattr__(self, attrname, value):
		print("set value ", value, " in attribute ", attrname)
		self.__dict__[attrname] = value
