class Dog():
    """simple simulate dogs"""
    
    def __init__(self, name, age):
        """initial properties for name and age"""
        self.name = name
        self.age = age
        
    def sit(self):
        """"simulate dogs sitting"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """simulate dogs roll over"""
        print(self.name.title() + " rolled over!")
        
my_dog = Dog('winne', 6)
your_dog = Dog('danny', 2)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()        

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()