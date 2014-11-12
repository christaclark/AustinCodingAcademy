class Person: 
	def __init__(self, name, age=None, class_name):
		# _init_ is a special character, typically something with underscores on either side is private, 
		# but 2 underscores on both sides can be imported as a module 
		self.name = name
		self.age = age
		self.class_name = class_name

	def is_old(self):
		if self.age < 30 
			return "Is not old"
		else: 
			return "Is old"	

#object is something that contains date (such as name & age) as well as functionality
instructorPerson = Person('Samir', 30)
print instructorPerson.name 
print instructorPerson.age 
#so we have created an object and have bound the name and age properties to the object "instructorPerson"


studentPerson = Person(name='Mark', age=21) 
print studentPerson.name
#if there are may variables you can declare the name perameters


# - - - - - - - - - - - VERSION 1  - - - - - - - - - - - - - - -  - - - - - - - - - - -

class Order:
	def __init__(sef, person_name, items):
		"""
		Order for Amazon
		:param string person_name: Who placed the order
		:param list(dict) items: These are items in your cart 
		:return: None
		"""
		self.pname = person_name 
		#This "person_name" is the name I want to reference with any code written below
		self.cart_items = items

	def get_order_total(self):
		"""
		This method gets our order total 
		:return: float
		"""

		order_total = 0.00
		for item in self.cart_items:
			order_total += item['price']
		return order_total



items = [
	{'item_id': 234, 'item_name': 'Keyboard': 'price': 12.45 }
	{'item_id': 564, 'item_name': 'Mouse': 'price': 4.54 }
	{'item_id': 876, 'item_name': 'Laptop': 'price': 1200.22 }]

myOrder = Order('Samir', items)

orderTotal = myOrder.get_order_total()

print "Order total: %f" % orderTotal


# - - - - - - - - - - - VERSION 2  - - - - - - - - - - - - - - -  - - - - - - - - - - -
# We are going to check to see if the order total won't overdraw their bank balance
class Person:
	def __init__(self, name, bank_balance):
		self.name = name  #use self because it defines the order class, the property is "person"
		self.balance = bank_balance
		"""
		Can this person afford the order?
		:param flaot order_total: What's the person's order total?
		:param list(dict) items: These are items in your cart 
		:return: None
		"""

	def can_afford(self, order_total):
		"""
		This method gets our order total 
		:return: float
		"""

		order_total = 0.00
		for item in self.cart_items:
			order_total += item['price']
		return order_total

def place_order(self):
	""" 
	Place the order, charge the car, write to the DB, send an email...
	:return: None
	"""
	if self.person.can_afford(self.get_order_total()):
		print "This person is stinkin rich"
	else:
		print "No compooter for you!"



items = [
	{'item_id': 234, 'item_name': 'Keyboard': 'price': 12.45 }
	{'item_id': 564, 'item_name': 'Mouse': 'price': 4.54 }
	{'item_id': 876, 'item_name': 'Laptop': 'price': 1200.22 }]

myPerson = Person('Samir', bank_balance=50.25)

myOrder = Order(myPerson, items) # What is the method signature? List of dictionaries needs to be defined

#orderTotal = myOrder.get_order_total()
myOrder.place_order()

#print "Order total: %f" % orderTotal

