'''Conditional Tests: Write a series of conditional tests Print a statement describing each test and your prediction for
 the results of each test '''

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



Pizzas = ['tuna', 'sardin', 'hemonta', 'fish']

for Pizza in Pizzas:
    if Pizza == 'fish':
        print(Pizza.upper())
    else:
        print(Pizza.title())



''' Imagine an alien was just shot down in a game Create a variable called alien_color and assign it a value of 'green',
'yellow', or 'red':

•	 Write an if statement to test whether the alien’s color is green If it is, print a message that the player just
earned 5 points
•	 Write one version of this program that passes the if test and another that fails (The version that fails will have
no output )
•	 If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
•	 If the alien’s color isn’t green, print a statement that the player just earned 10 points.
•	 Write one version of this program that runs the if block and another that runs the else block. '''


alien_colors = ['green', 'red', 'yellow']

if "green" in alien_colors:
    print('The Player has earned 5 ponits')
if "orrange" not in alien_colors:
    print('The player has earned 10 points')

if 'blue' in alien_colors:
    print("Player has upgraded")
else:
    print('sorry, you are unable\n \n')

if 'green' not in alien_colors:
    print('nothing')
else:
    print('The player has earned 5 points')

if 'red' in alien_colors:
    print('The player has earned 10 points')

if 'yellow' not in alien_colors:
    print('nothing')
elif 'yellow' in alien_colors:
    print('The player has earned 15 points\n \n')



'''Write an if-elif-else chain that determines a person’s stage of life Set a value for the variable age, and then:
•	 If the person is less than 2 years old, print a message that the person is a baby
•	 If the person is at least 2 years old but less than 4, print a message that the person is a toddler
•	 If the person is at least 4 years old but less than 13, print a message that the person is a kid
•	 If the person is at least 13 years old but less than 20, print a message that the person is a teenager
•	 If the person is at least 20 years old but less than 65, print a message that the person is an adult
•	 If the person is age 65 or older, print a message that the person is an elder'''

age = 65

if age < 2:
    print('The person is a baby')
elif age < 4:
    print('The person is a Tadler')
elif age < 13:
    print('The person is a Kid')
elif age < 20:
    print('The person is a Teenager')
elif age < 65:
    print('The person is an Adult')
elif age >64:
    print('The person is a Elder')

