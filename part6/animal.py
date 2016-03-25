class Animal:
	def speak(self):
		print("I am animal!")
	def reply(self):
		self.speak()

class Mammal(Animal):
	def speak(self):
		print("I am a mammal!")

class Cat(Mammal):
	def speak(self):
		print("I am a cat!")

class Dog(Mammal):
	def speak(self):
		print("I am a dog!")

class Primate(Mammal):
	def speak(self):
		print("I am a primate!")

class Hacker(Primate): pass
#	def speak(self):
#		print("I am a hacker!")

if __name__ == '__main__':
	c = Cat()
	c.reply()
	h = Hacker()
	h.reply()
