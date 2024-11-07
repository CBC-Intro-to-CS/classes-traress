class User1:
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

user1 = User1('Sam', 'Trares', 'male', 14)

user1.describe_user()
user1.greet_user() 

class User2:
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

user1 = User2('Connor', 'Smith', 'male', 97)

user1.describe_user()
user1.greet_user()

class User3:
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

user1 = User3('John', 'Phillips', 'male', 36)

user1.describe_user()
user1.greet_user()
