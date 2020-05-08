'''Use a dictionary to store information about a person you know Store their first name, last name, age, and the city in
 which they live You should have keys such as first_name, last_name, age, and city Print each piece of information stored
 in your dictionary'''



friend_info = {'first_name': 'Sayed', 'last_name':'Rasul', 'age': 29, 'city': 'Noakhali'}
print(friend_info)

print("My friend first name is: " + friend_info['first_name']+", his last name is: "+friend_info['last_name']+
      ", age: "+str(friend_info['age'])+ ", He lives in "+friend_info['city']+".")




'''Use a dictionary to store people’s favorite numbers Think of five names, and use them as keys in your dictionary 
Think of a favorite number for each person, and store each as a value in your dictionary Print each person’s name and
their favorite number For even more fun, poll a few friends and get some actual data for your program'''



favorite_numbers = { 'Shehab': 11, 'Sunvey': 22, 'Nayem': 33, 'Rana': 55, 'Masum': 67}

for name, number in favorite_numbers.items():
    print( name + "'s favorite number is: " + str(number))



'''Glossary: A Python dictionary can be used to model an actual dictionary However, to avoid confusion, let’s call it a
 glossary:
•	 Think of five programming words you’ve learned about in the previous chapters Use these words as the keys in your
glossary, and store their meanings as values
•	 Print each word and its meaning as neatly formatted output You might print the word followed by a colon and then
 its meaning, or print the word on one line and then print its meaning indented on a second line Use the newline character
  (\n) to insert a blank line between each word-meaning pair in your output'''



favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'php',
'phil': 'Java',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "! \n" )



'''Creating dictionary: Make 30 green aliens.'''

aliens = []

for aliennumber in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    print(aliens)