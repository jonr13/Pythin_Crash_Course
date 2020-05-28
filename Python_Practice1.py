class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #init is a method that automatically runs when an object is created
        # class attributes can be called
        # to create an attribute, the attribute must be the same name as the input
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}!")
        print(f"The {self.cuisine_type} sold here is amazing!")
        # f must be before the quotes
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")



class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
    def descriptive_name(self):
        print(f"The car is a {self.make}, of the year {self.year}, of the model {self.model}!")
    def update_odomoter(self, mileage):
        if mileage >= self.odomoter_reading:
            self.odomoter_reading = mileage
        else:
            print("You can't do that!")

my_new_car = Car("Toyota", "Rav4", 2008)
my_new_car.update_odomoter(20)
#call the method with mileage input
print(my_new_car.odomoter_reading)
#print the new variable


    

        