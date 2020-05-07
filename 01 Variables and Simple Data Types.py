# Simple Message: Store a message in a variable, and then print that message


name_of_students = "A B C D E F G H I J K L M N O P "
print(name_of_students)


# Store a message in a variable, and print that message. Then change the value of your variable to a new message, and print the new message.

name_of_students = "Q R S T U V W X Y Z"

print(name_of_students)

favorite_language = 'python '
print(favorite_language.rstrip())

favorit_language = ' C '
print(favorit_language.rstrip())
print(favorit_language.lstrip())

#.......................................

print("Python")

favoritee_language = 'pythoN. '
print(favoritee_language)
print(favoritee_language.rstrip())


'''Store a person’s name in a variable, and print a message to that person Your message should be simple, such as, “Hello Eric,
  would you like to learn some Python today?”'''

frined_name = "eric tush"

print("Hello " + frined_name.title() +", Would you like to learn some python today?")

print(frined_name.upper())

print(frined_name.lower())



'''Find a quote from a famous person you admire Print the quote and the name of its author Your output should look something like the
   following, including the quotation marks: 
   Albert Einstein once said, “A person who never made a mistake never tried anything new.” '''

qoute = 'Albert Einestain once said, "A person who never made a mistake never tried anything new"'
print(qoute)



'''Repeat last Exercise, but this time store the famous person’s name in a variable called famous_person Then compose your message
and store it in a new variable called message Print your message'''


famous_person = "Albert Einestain"

message = famous_person + ' once said, "A person who never made a mistake never tried anything new"'

print(message)



''' Store a person’s name, and include some whitespace characters at the beginning and end of the name Make sure you use each
character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip(). '''


name = " mr\tkhan\tbahadur\npirojpuri "
print(name)

print(name.lstrip())
print(name.rstrip())
print(name.strip())

BirthDay = "Happy 23rd BirthDay!"
print(BirthDay)

age = "28"
birthDay = "Happy "+ age +"rd birthday!"
print(birthDay)

birthday = "Happy "+ str(age) +"rd birthday!"
print(birthday)