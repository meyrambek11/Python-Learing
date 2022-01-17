class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("Person created")
	def say_hello(self):
		print(f"{self.name} says hello")

class Student(Person):
	def __init__(self,name,age,avg):
		super().__init__(name,age)
		self.avg = avg
	def study(self):
		print(f"{self.name} studies")
	def say_hello(self):
		print(f"{self.name} student says hello")
		print(self.avg)

class Teacher(Person):
	#super().__init__(name,age)
	def teach(self):
		print(f"{self.name} teaches")
	def say_hello(self):
		print(f"{self.name} teacher says hello")

def introduce(person):
	person.say_hello()

person_arr = [Student("Tom",18,4.5), Teacher("Katy",40), Student("Jony",19,4.0)]

for person in person_arr:
	introduce(person)