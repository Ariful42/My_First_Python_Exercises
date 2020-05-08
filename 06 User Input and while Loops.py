'''Write a program that asks the user what kind of rental car they would like Print a message about that car, such as
“Let me see if I can find you a Subaru ”'''

choice = input( "What kind of rental car You would like: ")
print("Let me see if I can find you a " + choice + "!")



'''Write a program that asks the user how many people are in their dinner group If the answer is more than eight, print 
a message saying they’ll have to wait for a table Otherwise, report that their table is ready'''

customer = input("how many people are in their dinner group: ")
customer = int(customer)

if customer > 8:
    print("You guys have to wait for a table!")
else:
    print("Yours table is ready")



'''Ask the user for a number, and then report whether the number is a multiple of 10 or not'''


values = input(" Input a number: ")
values = int(values)

if values % 10 == 0:
    print("Your number is multiple of 10.")
else:
    print("Your is not multiple of 10")



'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value As they enter
each topping, print a message saying you’ll add that topping to their pizza'''

prompt = ("Enter your Pizza toppings: ")
prompt += ("\nPress quit when you are finished ")

messege = ""
while messege != "quit":
    messege = input(prompt)
    if messege != "quit":
        print(messege.title() + " has been added!")


'''A movie theater charges different ticket prices depending on a person’s age If a person is under the age of 3, the 
ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15 Write a 
loop in which you ask users their age, and then tell them the cost of their movie ticket'''


promt = ("Press 0 when you are finish!")
promt += ("\nInsert your age: ")
age = ""
while age != "0":
    age = input(promt)
    age = int(age)
    if age == 0:
        break
    elif age < 3 :
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket price is $10. ")
    else:
        print("Your ticket price is $15. ")


'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called 
finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your 
tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been
made, print a message listing each sandwich that was made'''

sandwich_order = ['butter','pastrami', 'cheese','pastrami',  'chicken', 'mutton','pastrami', 'beef']
finished_sandwich = []

while sandwich_order:
    preparing = sandwich_order.pop()
    print(preparing.title() + " is being prepared.")
    finished_sandwich.append(preparing)
print("Following Sandwiches has been prepared. ")
for finished_sandwichs in finished_sandwich:
    print(finished_sandwichs.title())


'''Using the list sandwich_orders from last Exercise, make sure the sandwich 'pastrami' appears in the list at least 
three times Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and 
then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end 
up in finished_sandwiches'''

finished_sandwic = ['butter','pastrami', 'cheese','pastrami', 'chicken', 'mutton','pastrami', 'beef']
print("\n \nDelhi is running out of Pastrami.")

while 'pastrami' in finished_sandwic:
    finished_sandwic.remove('pastrami')
print(finished_sandwic)



'''Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in
the world, where would you go? Include a block of code that prints the results of the poll'''


places = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("In which place do you want to make your vacation? ")
    places[name] = place
    repeat = input("Would you like to give your friends to make decision? (yes/no)")
    if repeat == "no" :
        polling_active = False
print(".......Results of choices are following: ")
for name, place in places.items():
    print(name + " like to go " + place + ".")