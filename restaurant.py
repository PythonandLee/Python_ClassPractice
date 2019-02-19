class Restaurant():
    """simulate restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("\nThis restaurant, " + self.restaurant_name.title() + ", has " +
          self.cuisine_type.title() + " cuisines.")
        if self.number_served == 0:
            pass
        else:      
            print("They have had " + str(self.number_served) + " guests.")
    
    def open_restaurant(self):
        print("The restaurant is now openinig.")
        
    def set_served_number(self, num):
        self.number_served = num
        
    def increment_number_served(self):
        """new 100 guests come everyday"""
        self.number_served += 100
        print("Till today, they have " + str(self.number_served) + " guests.")
        
restaurant = Restaurant("po's kitchen", 'korean') 
restaurant.set_served_number(1200) 
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_b = Restaurant('lady jen', 'american')
restaurant_b.describe_restaurant()

restaurant_c = Restaurant("rogger's", 'italian')
restaurant_c.set_served_number(800)
restaurant_c.describe_restaurant()
restaurant_c.increment_number_served()
restaurant_c.increment_number_served()
restaurant_c.increment_number_served()
restaurant_c.increment_number_served()
restaurant_c.increment_number_served()