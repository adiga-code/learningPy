class Car():
	"""Простая модель автомобиля"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometr_reading = 0
	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	def read_odometr(self):
		print(f"This car has {self.odometr_reading} kilometrs on it")
	def update_odometr(self, kilometrs):
		if kilometrs >= self.odometr_reading:
			self.odometr_reading = kilometrs
		else:
			print("You can't roll back an odometr!!!")
	def increment_odometr(self, kilometr):
		self.odometr_reading += kilometr
class ElectricCar(Car):
	"""Представляет аспекты машин, специфические для электрокаров"""
	def __init__(self, make, model, year):
		"""
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        """
		super().__init__(make, model, year)
		self.battery_size = 75
	def describe_battery(self):
		"""Выводит сообщение о мощности аккумулятора"""
		print(f"This car has {self.battery_size}-kWh battery.")
	def fill_gas_tank(self):
		"""У электромобилей нет бензобака"""
		print("This car don't need a gas tank!")
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
		
    	



































