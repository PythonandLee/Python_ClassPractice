class Car():
    """simple simulate cars"""
    def __init__(self, make, model, year):
        """initial car's properties"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
         """return descriptive informations"""
         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
         return long_name.title()
         
    def read_odometer(self):
        """print car's odometer miles"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")     
     
    def update_odometer(self, mileage):
        """set mileage to odometer and aovid to set back"""
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
             print("\nYou can't roll back an odometer!")
     
         
class Battery():
    """simulate battery"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """initial class 'Car' properties"""
        super().__init__(make, model, year)
        self.battery = Battery()

         
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()