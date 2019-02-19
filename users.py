class User():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self):
        print("\nUser " + self.first_name.title() + ", you are logging.")
        
    def greet_user(self):
        print("Hello " + self.first_name.title() +' ' + 
          self.last_name.title() + ", welcome!")
          
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Attempt logging: " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0      
        print("Attempt logging: " + str(self.login_attempts))
                  
user_a = User('danny', 'king')
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.increment_login_attempts()
user_a.describe_user()
user_a.greet_user()
user_a.reset_login_attempts()

user_b = User('lily', 'chen')
user_b.describe_user()
user_b.greet_user()

user_c = User('louise', 'king')
user_c.describe_user()
user_c.greet_user()