class Person:
	def setName(self, name):
		self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print ("Hello, world! I'm", self.name)

foo = Person()
bar = Person()
foo.setName('Uncle')
bar.setName('John')
foo.greet()
bar.greet()
