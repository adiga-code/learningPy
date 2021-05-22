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
