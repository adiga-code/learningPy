class Car():
	"""Простая модель автомобиля"""
	def __init__(self, make, model, year):
		self.make = make			
		self.model = model
		self.year = year
		self.odometr_reading = 0
	def read_odometer(self):
		"""Выводит пробег машины"""
		print(f"This car has {self.odometr_reading} kilometers on it")
	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание"""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name
	def update_odometr(self, number):
		"""Устанавливает заданное значение на одометре"""
		"""Проверяется изменение одометра в обратную сторону"""
		if number >= self.odometr_reading:
			self.odometr_reading = number
		else:
			print("You can't roll back an odometr")
	def increment_odometr(self, kilometers):
		self.odometr_reading += kilometers
car_bmw = Car("BMW", "M5", 2021)
print(car_bmw.get_descriptive_name())
car_bmw.read_odometer()
#Изменение значения одометра
car_bmw.update_odometr(33_000)
car_bmw.read_odometer()
#Увеличение показания одометра методом"""
car_bmw.increment_odometr(20_000)
car_bmw.read_odometer()



































