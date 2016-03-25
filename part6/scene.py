class Scene:
	def __init__(self):
		self.cust = Customer()
		self.cle = Clerk()
		self.par = Parrot()

	def action(self):
		for x in (self.cust, self.cle, self.par):
			x.line()

class Customer:
	def line(self):
		print("I am a customer!")

class Clerk:
	def line(self):
		print("I am a clerk!")

class Parrot:
	def line(self):
		print("I am a parrot!")

if __name__ == '__main__':
	sc = Scene()
	sc.action()
