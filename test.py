class Car():
	"""Простая модель автомобиля"""
	def __init__(self, make, model, year):
		self.make = make			
		self.model = model
		self.year = year
		self.read_odometer = 0
	def odometr_reading(self):
		"""Выводит пробег машины"""
		print(f"This car has {self.read_odometer} kilometers on it")
	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name
car_bmw = Car("BMW", "M5", 2021)
print(car_bmw.get_descriptive_name())
car_bmw.odometr_reading()

































