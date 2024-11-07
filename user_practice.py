class User:
    def __init__(self, first_name, last_name, gender, age):
        #initialize first name and last name
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age 
        self.gender = gender
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.gender} and is {self.age} years old.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name} welcome!")

user1 = User('Sam', 'Trares', 'male', 14)
user1.describe_user()
user1.greet_user() 

user2 = User('Connor', 'Smith', 'male', 97)
user2.describe_user()
user2.greet_user()

user3 = User('John', 'Phillips', 'male', 36)
user3.describe_user()
user3.greet_user()
