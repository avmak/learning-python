class Lunch:
	def __init__(self):
		self.cust = Customer()
		self.emp = Employee() 
	def order(self, foodName):
		print("Process of execution of the order.")
		self.cust.placeOrder(foodName, self.emp)
	def result(self):
		self.cust.printFood()

class Customer:
	def __init__(self):
		self.meal = None
	def placeOrder(self, foodname, employee):
		print("Order is passed to the waiter.")
		self.meal = employee.takeOrder(foodname)
	def printFood(self):
		print("My order is ", self.meal.dish, "")

class Employee:
	def takeOrder(self, foodName):
		print("Dish is ready!")
		return Food(foodName)

class Food:
	def __init__(self, name):
		self.dish = name

if __name__ == '__main__':
	x = Lunch()
	x.order('meat')
	x.ready()
