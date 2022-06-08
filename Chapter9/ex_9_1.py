class Restaurant:
    """A class representing a real world restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and type of food"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Print facts about restaurant"""
        print(f"The restaurant is named {self.restaurant_name}.")
        print(f"The restaurant serves {self.cuisine_type.lower()}.")
        
    def open_restaurant(self):
        """Prints a message that restaurant is open"""
        print(f"{self.restaurant_name} is now open for business!")
        
    def set_number_served(self, new_number_served):
        """Change number_served to provided value"""
        self.number_served = new_number_served
        
    def increment_number_served(self, increment_amount):
        """Increment number_served by provided value"""
        self.number_served += increment_amount

my_restaurant = Restaurant('Applebees', 'American')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

print(my_restaurant.number_served)

my_restaurant.set_number_served(15)

print(my_restaurant.number_served)

my_restaurant.increment_number_served(12)

print(my_restaurant.number_served)