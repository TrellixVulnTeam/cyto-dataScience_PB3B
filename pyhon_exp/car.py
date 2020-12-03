
class Car():
    """ A simple attempt to represent a car """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """ Represents aspects of a car, specific to electric vehicles. """

    def __init__(self, make, model, year, color):
        """ Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.color = color
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size. """
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def describe_color(self):
        print("The color of this car is " + self.color)

my_tesla = ElectricCar('Tesla', 'Model S', 2000, 'Black')

my_tesla.describe_battery()

my_tesla.read_odometer()
my_tesla.describe_color()