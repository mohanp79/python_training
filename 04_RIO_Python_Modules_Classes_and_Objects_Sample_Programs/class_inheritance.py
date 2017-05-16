class Person:
	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print ("Hello, world! I'm %s",self.name)

foo = Person()
bar = Person()
test = Person()
foo.setName('Uncle')
bar.setName('John')
test.setName('Python')
foo.greet()
bar.greet()
test.greet()
