from Car import Car
class Battery():
    """Простая модель аккумулятора автомобиля"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        """Выводит сообщение о мощности аккумулятора"""
        print(f"This car has {self.battery_size}-kWh battery.")
    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 75:
            range = 260
        if self.battery_size == 100:
            range = 315
        print(f'This car can go about {range} miles on a full charge')
class ElectricCar(Car):
    """Представляет аспекты машин, специфические для электрокаров"""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля
        """
        super().__init__(make, model, year)
        self.battery = Battery()