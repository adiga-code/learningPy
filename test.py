class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Restaurant '{self.restaurant_name} is good.")
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} has {self.cuisine_type} type.")
#класс-потомок класса Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanila', 'fistashki']
    def describe_flavors(self):
        print(f"\nWe have this flavors:")
        for flavor in self.flavors:
            print(flavor) 

restaurant1 = IceCreamStand('Ice creams', 'kafe ice cream')
print(restaurant1.open_restaurant())
restaurant1.describe_flavors()



































