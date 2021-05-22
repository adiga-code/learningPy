from Car import Car
from electric_car import ElectricCar as EC

my_bmw = Car('BMW', 'M5', 2021)
print(my_bmw.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

