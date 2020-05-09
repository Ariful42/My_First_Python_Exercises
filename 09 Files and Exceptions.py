'''Open a blank file in your text editor and write a few. lines summarizing what you’ve learned about Python so far
Start each line with the phrase In Python you can... Save the file as learning_python.txt in the same directory as your
exercises from this chapter Write a program that reads the file and prints what you wrote three times Print the contents
once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and
then working with them outside the with block'''

with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

print("\n")

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")

with open('learning_python.txt') as file_object:
    lines = file_object.readline()

for line in lines:
    print(line.rstrip())

print("\n")

with open('learning_python.txt') as file_object:
    lines = file_object.readline()

file_string = ''
for line in lines:
    file_string += line.rstrip()

print(file_string)
print(len(file_string))

print("\n")


'''You can use the replace() method to replace any word in a string with a different word Here’s a quick example 
showing how to replace 'dog' with 'cat' in a sentence. Read in each line from the file you just created, 
learning_python.txt, and replace the word Python with the name of another language, such as C Print each modified line 
to the screen'''


with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'C'))

message = "I really like dogs."
print(message.replace('dog', 'cat'))



'''Write a program that prompts the user for their name When they respond, write their name to a file called guest.txt'''


filename = 'guest.txt'

guest_name = input("Write your full name: ")

with open(filename, 'a') as file_object:
    file_object.write(guest_name.title() +"\n")



''' Write a while loop that prompts users for their name When they enter their name, print a greeting to the screen and
add a line recording their visit in a file called guest_book.txt Make sure each entry appears on a new line in the file'''


while True:
    guest = input("Input your full name: ")
    if guest == 'q':
        break
    print("Welcome Mr " + guest.title() + " to our Guest house!")
    book = 'guest_book.txt'
    with open(book, 'a') as g_book:
        g_book.write(guest.title() + " visited our guest house. \n")



