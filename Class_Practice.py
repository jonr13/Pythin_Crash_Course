class Restaurant():
    number_served = 1
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}!")
        print(f"The {self.cuisine_type} sold here is amazing!")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    def set_number_served(self, customers):
        self.number_served = customers
    def increment_number_served(self, number):
        self.number_served += number

class User:
    login_attempts = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def user_information(self):
        print(f"{self.first_name} {self.last_name}")
    def greeting(self):
        print(f"Welcome {self.first_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

jon = User('Jon', 'Rodriguez')
jon.increment_login_attempts()
print(jon.login_attempts)
jon.reset_login_attempts()
print(jon.login_attempts)

restaurant = Restaurant("Jason Deli", "Deli Food")

class IceCreamStand(Restaurant):
    flavors = ['vanilla', 'chocolate', 'strawberry']
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
    def display_flavors(self):
        print(self.flavors)

big_gay_icecream = IceCreamStand('Big Gay Icecream', 'Icecream')
print(big_gay_icecream.restaurant_name)
big_gay_icecream.display_flavors()

    
    
