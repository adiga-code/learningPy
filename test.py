class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name} is good.")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} has {self.cuisine_type} type.")
    def print_number_served(self):
    	print(f"{self.number_served} people are was there")
    """метод, позволяющий задать количество обслуженных посетителей"""
    def set_number_served(self, served):
    	self.number_served = served
    """метод, приращающий значение атрибута"""
    def increment_number_served(self, increment_served):
    	self.number_served += increment_served
restaurant1 = Restaurant("In_time", "sushi")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
#Выводит количкество людей, бывавших в ресторане
restaurant1.print_number_served()
#Изменяется количество людей, побывавших в ресторане прямым изменением значения атрибута
number_served = 10
restaurant1.print_number_served()
#Изменяется количество людей, побывавших в ресторане изменением значения аргумента методом
restaurant1.set_number_served(20)
restaurant1.print_number_served()
#изменяется количество людей, побывавших в ресторане приращением
restaurant1.increment_number_served(13)
restaurant1.print_number_served()




































