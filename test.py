class Dog():
	"""Простая модель собаки"""
	def __init__(self , name , age):
		self.name = name
		self.age = age
	def sit(self):
		print(f"{self.name} is now sitting. ")
	def roll_over(self):
		print(f"{self.name} roll over! ")
"""Создаём экземпляр класса"""		
my_dog = Dog("Dgek", 11)
"""Обращение к атрибутам"""
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age}.")
"""Вызов методов"""
my_dog.sit()
my_dog.roll_over()




































































