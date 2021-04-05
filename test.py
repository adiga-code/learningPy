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

class Battery():
    """Простая модель аккумулятора автомобиля"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит сообщение о мощности аккумулятора"""
        print(f"This car has {self.battery_size}-kWh battery.")
    def upgrade_battery(self, number):
        if self.battery_size > number:
            self.battery_size += number
        else:
            self.battery_size = 100
            print("OI OI OI") 
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 60:
            ran_ge = 260
        elif self.battery_size == 100:
            ran_ge = 315
        else:
            ran_ge = 300

        print(f'This car can go about {ran_ge} miles on a full charge')

class ElectricCar(Car):

    """Представляет аспекты машин, специфические для электрокаров"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """У электромобилей нет бензобака"""
        print("This car don't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery(25)
my_tesla.battery.get_range()

































