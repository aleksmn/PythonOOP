# Class programming in Python


class Person():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def say_something(self):
		print(f"{self.name} says 'Hi!'")

class Student(Person):
	def __init__(self, name, age, grade):
		Person.__init__(self, name, age)
		self.grade = grade		
	def say_something(self):
		print(f"{self.name} says 'Is this on the test?'")

class Teacher(Person):
	def __init__(self, name, age, department):
		Person.__init__(self, name, age)
		self.department = department		
	def say_something(self):
		print(f"{self.name} says 'Please, mute your mic!'")
		
bob = Person("Bob", 42)
sue = Student("Sue", 22, 2)
jason = Teacher("Jason", 50, "Art department")

people = [bob, sue, jason]

for person in people:
	print(f"{person.name} is {person.age} years old.")
	if isinstance(person, Student):
		print(f"{person.name} is in grade {person.grade}.")
	if isinstance(person, Teacher):
		print(f"{person.name} is in {person.department} department.")
	person.say_something()
	print("")






