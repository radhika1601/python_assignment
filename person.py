class Person:

	def __init__(self, name, city="Roorkee", *args):
		self.name = name
		self.city = city
		if bool(args):
			self.work = args[0]
		
	
	def show(self):
		print("My name is {0} and my current city is {1}".format(
			self.name,
			self.city))


# p1 = Person("radhika", "balotra","student")
# p1.show()
# print(p1.work)
# p2 = Person('surya')
# p2.show()
# print(p2.work)