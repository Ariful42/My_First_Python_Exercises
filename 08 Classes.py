'''Make a class called Restaurant The __init__() method for Restaurant should store two attributes: a restaurant_name
and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method
called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called
restaurant from your class. Print the two attributes individually, and then call both methods'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ". \n")
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " type restaurant.\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open 24 hours every day!")


my_restaurant = Restaurant('art of island', 'five star')
print(my_restaurant.restaurant_name.title() + " is my restaurant!")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()



'''Start with your class from last Exercise. Create three different instances from the class, and call describe_restaurant()
for each instance'''

your_restaurant = Restaurant('Alaska', 'three start')
his_restaurant = Restaurant('soloman', 'two start')
frind_restaurant = Restaurant('saldrin', 'one start')

your_restaurant.describe_restaurant()
his_restaurant.describe_restaurant()
frind_restaurant.describe_restaurant()



'''Make a class called Use Create two attributes called first_name and last_name, and then create several other 
attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user'''

class Use():
    def __init__(self, first_name, last_name, age, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = age
        self.designation = designation

    def describe_user(self):
        print(self.full_name.title() + "is an engineer and He is " + str(self.age) + " years old and also he is a "
              + self.designation.title() + ".")

    def greet_user(self):
        print("Hello Dr " + self.full_name.title() + '!')

doctor = Use('eric', 'busto', 30, 'phd')
print(doctor.first_name.title() + " is my first name.")
doctor.describe_user()
doctor.greet_user()


'''Start with your program from first Exercise. Add an attribute called number_served with a default value of 0. Create 
an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change 
this value and print it again. Add a method called set_number_served() that lets you set the number of customers that 
have been served. Call this method with a new number and print the value again. Add a method called increment_number_served()
that lets you increment the number of customers who’ve been served. Call this method with any number you like that could
represent how many customers were served in, say, a day of business'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ". \n")
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " type restaurant.\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open 24 hours every day!")

    def served_number(self):
        print("The number served by the " + self.restaurant_name.title() + " restaurant are " + str(self.number_served)
              + "!")

    def set_number_served(self, numbers):
        self.number_served = numbers

    def increment_number_served(self, number):
        self.number_served += number
        print("In one day, number of served customer are " + str(number) + "!")

restaurant = Restaurant('art of island', 'five star')
restaurant.served_number()

restaurant.number_served = 500
restaurant.served_number()

restaurant.set_number_served(1000)
restaurant.served_number()

restaurant.increment_number_served(200)
restaurant.served_number()



'''Add an attribute called login_attempts to your User class from Exercise. Write a method called increment_login_attempts()
that increments the value of login_attempts by 1 Write another method called reset_login_attempts() that resets the 
value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print
login_attempts again to make sure it was reset to 0'''


class Use():
    def __init__(self, first_name, last_name, age, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = age
        self.designation = designation
        self.login_attemts = 0

    def describe_user(self):
        print(self.full_name.title() + "is an engineer and He is " + str(self.age) + " years old and also he is a "
              + self.designation.title() + ".")

    def greet_user(self):
        print("Hello Dr " + self.full_name.title() + '!')

    def increment_login_attemts(self):
        self.login_attemts += 1
        print("The number of login attempts are " + str(self.login_attemts) + "!")

    def reset_login_attempts(self):
        if self.login_attemts > 0:
            self.login_attemts = 0
            print("The login attemts reset to " + str(self.login_attemts) + "!")

use = Use('eric', 'bost', 26, 'phd')
use.increment_login_attemts()
use.increment_login_attemts()
use.increment_login_attemts()
use.reset_login_attempts()
use.increment_login_attemts()


'''An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the 
Restaurant class you wrote in previous Exercises. Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.'''


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ". \n")
        print(self.restaurant_name.title() + " is a " + self.cuisine_type + " type restaurant.\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open 24 hours every day!")


my_restaurant = Restaurant('art of island', 'five star')
print(my_restaurant.restaurant_name.title() + " is my restaurant!")

class Ice_cream_stand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.names = ['mania', 'vanila', 'mango', 'strawberry']

    def print_ice_cream_flavors(self, names):
        for flavor in names:
            msg = "We have " + flavor + " Icre cream!"
            print(msg)

iceCream = Ice_cream_stand('art', 'five')
#iceCream.names = ['mania', 'vanila', 'mango', 'strawberry']
print(iceCream.print_ice_cream_flavors(iceCream.names))



'''An administrator is a special kind of user Write a class called Admin that inherits from the User class you wrote in 
previous Exercises. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", 
"can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges.
Create an instance of Admin, and call your method'''


class User():
    def __init__(self, first_name, last_name, age, designation):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.age = age
        self.designation = designation

    def describe_user(self):
        print(self.full_name.title() + "is an engineer and He is " + str(self.age) + " years old and also he is a "
              + self.designation.title() + ".")

    def greet_user(self):
        print("Hello Dr " + self.full_name.title() + '!')

doctor = User('eric', 'busto', 26, 'phd')

class Admin(User):
    def __init__(self, first_name, last_name, age, designation):
        super().__init__(first_name, last_name, age, designation)
        self.privilages = ["can add post", "can delete post", "can ban user"]
        self.privilage = Privilages(self.privilages)


    def show_privilages(self, privilages):
        for privilage in privilages:
            print("One of the privilages is " + privilage + "!")

admin = Admin('eric', 'bruto', 26, 'phd')
print(admin.show_privilages(admin.privilages))



'''Write a separate Privileges class The class should have one attribute, privileges, that stores a list of strings as
described in Exercises. Move the show_privileges() method to this class Make a Privileges instance as an attribute in 
the Admin class Create a new instance of Admin and use your method to show its privileges'''


class Privilages():
    def __init__(self, privilages):
        self.privilages = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self, privilages):
        for privilage in privilages:
            print("One of the privilages is " + privilage + "!")

my_privilage = Admin('eric', 'bruto', 26, 'phd')
print(my_privilage.privilage.show_privilages(my_privilage.privilages))



'''Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery()
This method should check the battery size and set the capacity to 85 if it isn’t already. Make an electric car with a 
default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery You 
should see an increase in the car’s range'''

class Battery():
    def __init__(self, battery_size = 70):