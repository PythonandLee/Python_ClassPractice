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
         
         
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())    
     
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_new_car.update_odometer(6)
my_new_car.read_odometer()