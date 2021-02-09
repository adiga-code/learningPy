class Dog():
	"""Простая модель собаки"""
	def __init__(self , name , age):
		self.name = name
		self.age = age
	def sit(self):
		print(f"{self.name} is now sitting. ")
	def roll_over(self):
		print(f"{self.name} roll over! ")
my_dog = Dog("Dgek", 11)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age}.")




































































