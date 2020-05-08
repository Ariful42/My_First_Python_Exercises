'''Write a function called display_message() that prints one sentence telling everyone what you are learning about in
this chapter Call the function, and make sure the message displays correctly'''

def display_message():
    print("Hello, I am learning function in this chapter.")

display_message()



'''Write a function called favorite_book() that accepts one parameter, title The function should print a message, such 
as One of my favorite books is Alice in Wonderland Call the function, making sure to include a book title as an argument 
in the function call'''

def favorite_book(book):
    print("My favorite book name is " + book.title() + ".")
favorite_book("Al Quran")



'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the 
shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the 
function once using positional arguments to make a shirt. Call the function a second time using keyword arguments'''

def make_shirt(type, size):
    print("\nThe " + type.title() + " type shirt size is " + size + "!")

make_shirt('Domain','35')
make_shirt(type = 'Jack and Jones', size = 'XL')
make_shirt(size = 'XXL', type = 'not domain')



'''Modify the make_shirt() function so that shirts are large by default. Make a large shirt and a medium shirt with the 
default message, and a shirt of any size with a different message'''

def make_shirt(type, size = 'L'):
    print("\nThe " + type.title() + " type shirt size is " + size + "!")

make_shirt('Domain')
make_shirt(type = 'Domain', size = 'M')



'''Write a function called describe_city() that accepts the name of a city and its country. The function should print a 
simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function 
for three different cities, at least one of which is not in the default country'''


def describe_city(city, country = 'Bangladesh'):
    print("\nThe " + city.title() + " is one of the notable place in " + country.title() + ".")

describe_city('dhaka')
describe_city('Rangpur')
describe_city(city = 'lalmonirhat', country = 'world')



'''Write a function called city_country() that takes in the name of a city and its country. Call your function with at 
least three city-country pairs, and print the value that’s returned'''


def city_country(city_name, country_name):
    full_output = city_name + ' , ' + country_name
    return full_output.title()

C_Country = city_country('Lalmonirhat', 'Bangladesh')
print(C_Country)

CC_Country = city_country('Berlin','Germany')
print(CC_Country)

CCC_Country = city_country('Paris', 'France')
print(CCC_Country)



'''Write a function called make_album() that builds a dictionary describing a music album. The function should take in an 
artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the 
function to make three dictionaries representing different albums. Print each return value to show that the dictionaries 
are storing the album information correctly. Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s 
dictionary. Make at least one new function call that includes the number of tracks on an album'''

def make_album(artist, title, tracks = ''):
    album = {'Artist_name' : artist, 'Album_Title' : title}
    if tracks:
        album['tracks']= tracks
    return album
D_result = make_album('Dudo', 'Cattish')
print(D_result)

print(make_album('Rudo', 'Lattish'))
print(make_album('Kudo', 'Mattish'))
print(make_album('Arif', 'Hamdibari', '17'))



'''Start with your program from last Exercise. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure 
to include a quit value in the while loop'''


while True:
    print('\nPlease give the album details:')
    print("Press Q when you finish.")

    ar_name = input('Artist_Name: ')

    if ar_name == 'Q':
        break

    al_title = input('Album_Title: ')

    if al_title == 'Q':
        break

    print(make_album(ar_name, al_title))



'''Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each 
magician in the list'''


def show_magician(magicians):
    for magician in magicians:
        print("Hello " + magician.title() + '!')

Magician = ['Tourse', 'jorests', 'bhdiskji', 'hysgiuyqt']

show_magician(Magician)



'''Start with a copy of your program from last Exercise. Write a function called make_great() that modifies the list of 
magicians by adding the phrase the Great to each magician’s name Call show_magicians() to see that the list has actually
been modified'''


def make_great(Magician, modified_names):

    while Magician:

        Current_name = Magician.pop()
        print("Great to " + Current_name.title() + "!" )
        modified_names.append(Current_name)

modified_names = []
make_great(Magician, modified_names)
show_magician(Magician)



'''Start with your work from last Exercise. Call the function make_great() with a copy of the list of magicians’ names 
Because the original list will be unchanged, return the new list and store it in a separate list. Call show_magicians() 
with each list to show that you have one list of the original names and one list with the Great added to each magician’s
name'''

def make_great(Magician, modified_names):

    while Magician:

        Current_name = Magician.pop()

        print("Great to " + Current_name.title() + "!" )

        modified_names.append(Current_name)

Magician= ['Tourse', 'jorests', 'bhdiskji', 'hysgiuyqt']
modified_names = []
make_great(Magician[:], modified_names)



'''Write a function that accepts a list of items a person wants on a sandwich The function should have one parameter 
that collects as many items as the function call provides, and it should print a summary of the sandwich that is being 
ordered Call the function three times, using a different number of arguments each time'''


def make_sandwich(*ingredients):
    print("\n Making a Sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print("-" + ingredient.title())

make_sandwich('Butter', 'bread', 'chicken', 'masroom')

make_sandwich('bread', 'beef', 'ponir', 'tometo')

make_sandwich('bread', 'puten', 'masroom', 'makhon')


'''Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your
first and last names and three other key-value pairs that describe you'''

def build_profile(first, last, **user_info):

    profile = {}
    profile['First_name '] = first.title()
    profile['Last_name '] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile('arif', 'islam', Location = 'Germany')

print(my_profile)



'''Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer
and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required 
information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call 
like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.'''


def make_car(manufacturer, model_name, **car_info):

    Car = {}
    Car['Manufacturer_Name '] = manufacturer
    Car['Model_Car '] = model_name
    for key, value in car_info.items():
        Car[key] = value
    return Car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(" \nYour expected car information are as below")
print(car)



'''Put the functions for the example print_models.py in a separate file called printing_functions.py Write an import 
statement at the top of print_models.py, and modify the file to use the imported functions'''

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



'''Using a program you wrote that has one function in it, store that function in a separate file Import the function 
into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import'''

from pizza import build_profile

my_profile = build_profile('arif', 'islam', Location = 'Germany')
print(my_profile)

from pizza import build_profile as bp
my_profile = bp('arif', 'islam', Location = 'Germany')
print(my_profile)

import pizza as p
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

my_profile = build_profile('arif', 'islam', Location = 'Germany')
print(my_profile)

