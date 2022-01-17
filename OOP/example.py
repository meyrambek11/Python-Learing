class Animal:
	def __init__(self,name):
		self.name = name
	def eat(self):
		print(f"{self.name} eating")

class Dog(Animal):
	def __init__(self,name,breed):
		super().__init__(name)
		self.breed = breed
	def bark(self):
		print(f"{self.name} is barking")

class Cat(Animal):
	def meow(self):
		print(f"{self.name} meow")

class Frog(Animal):
	def eat(self):
		print(f"{self.name} frog is eating")

def introduce(self):
	self.eat()

animal_arr = [Dog("Ashkon","Nemes"), Cat("Ashkonay"), Frog("Frog")]

for anim in animal_arr:
	introduce(anim)
