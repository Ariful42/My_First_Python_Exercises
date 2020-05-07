'''Store the names of a few of your friends in a list called names Printeach person’s name by accessing each element
 in the list, one at a time. Instead of just printing each person’s name, print a message to them The text of each
 message should be the same, but each message should be personalized with the person’s name'''

names = ['kamrul', 'nur', 'oli', 'halim']
print(names[0])
print(names[-1])
print(names[1])
print(names[2])

print("" + names[0].title() + " is invited to our meeting")
print("" + names[1].title() + " is invited to our meeting")
print(""+names[2].title()+" and "+names[-1].title()+" are also invited to our meeting")


'''If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least 
three people you’d like to invite to dinner Then use your list to print a message to each person, inviting them to dinner'''

Dinner = ['shehab', 'iqbal', 'nayeem', 'masum']

print(""+ Dinner[0].title() +", you are invited to my diinner")
print(""+Dinner[1].title() +", you are invited to my dinner")
print(""+Dinner[2].title()+", you are invited to my dinnwe")
print(""+Dinner[3].title()+", you are invited to my dinner")


'''You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations 
You’ll have to think of someone else to invite'''

print(""+ Dinner[0].title() +", You are deleted from the list of dinner")
print(""+ Dinner[1].title() +", Rahim won't come to dinner")
print(""+ Dinner[2].title()+", Rahim won't come to dinner")
print(""+ Dinner[3].title()+", Rahim won't come to dinner")

Dinner[0] = 'Zahed'

print(Dinner)

print(""+ Dinner[0].title() +", You are still in the list of dinner")
print(""+Dinner[1].title() +", You are still in the list of dinner")
print(""+Dinner[2].title()+",You are still in the list of dinner")
print(""+Dinner[3].title()+", You are still in the list of dinner")



'''You just found a bigger dinner table, so now more space is available Think of three more guests to invite to dinner'''

print("\n")
print(""+ Dinner[0].title() +", I have found a big table so more people will be added")
print(""+Dinner[1].title() +", I have found a big table so more people will be added")
print(""+Dinner[2].title()+",I have found a big table so more people will be added")
print(""+Dinner[3].title()+", I have found a big table so more people will be added")

Dinner.insert(0, 'aman')
Dinner.insert(3, 'rana')
Dinner.append('sunvy')

print("\n"+ Dinner[0].title() +", you are invited to my diinner")
print(""+Dinner[1].title() +", you are invited to my dinner")
print(""+Dinner[2].title()+", you are invited to my dinner")
print(""+Dinner[3].title()+", you are invited to my dinner")
print(""+ Dinner[4].title() +", you are invited to my diinner")
print(""+Dinner[5].title() +", you are invited to my dinner")
print(""+Dinner[6].title()+", you are invited to my dinner")


'''You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests'''

print("\n"+ Dinner[0].title() +", The big table won't come and I can only invite two person")
print(""+Dinner[1].title() +", The big table won't come and I can only invite two person")
print(""+Dinner[2].title()+", The big table won't come and I can only invite two person")
print(""+Dinner[3].title()+",The big table won't come and I can only invite two person")
print(""+ Dinner[4].title() +",The big table won't come and I can only invite two person")
print(""+Dinner[5].title() +", The big table won't come and I can only invite two person")
print(""+Dinner[6].title()+", The big table won't come and I can only invite two person")

print(Dinner)

Popped_name1 = Dinner.pop(0)
Popped_name2 = Dinner.pop(0)
Popped_name3 = Dinner.pop(0)
Popped_name4 = Dinner.pop(0)
Popped_name5 = Dinner.pop(0)

print("\n"+Popped_name1.title() +", I am sorry, you aren't in the list of Dinner")
print(""+Popped_name2.title() +", I am sorry, you aren't in the list of Dinner")
print(""+Popped_name3.title() +", I am sorry, you aren't in the list of Dinner")
print(""+Popped_name4.title() +", I am sorry, you aren't in the list of Dinner")
print(""+Popped_name5.title() +", I am sorry, you aren't in the list of Dinner")

print("\n"+Dinner[0].title() +", You are still in the list of dinner")
print(""+Dinner[1].title()+", You are still in the list of dinner")

del Dinner[0]
del Dinner[0]

print(Dinner)


'''Seeing the World: Think of at least five places in the world you’d like to visit:
•	 Store the locations in a list Make sure the list is not in alphabetical order
•	 Print your list in its original order Don’t worry about printing the list neatly, just print it as a raw Python list
•	 Use sorted() to print your list in alphabetical order without modifying the actual list
•	 Show that your list is still in its original order by printing it
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list
•	 Show that your list is still in its original order by printing it again
•	 Use reverse() to change the order of your list Print the list to show that its order has changed
•	 Use reverse() to change the order of your list again Print the list to show it’s back to its original order
•	 Use sort() to change your list so it’s stored in alphabetical order Print the list to show that its order has been changed
•	 Use sort() to change your list so it’s stored in reverse alphabetical order Print the list to show that its order has changed'''


location = [ "Prague", "France", "Turkey", "Italy", "Roam"]

print(location)
print(sorted(location))

print(location)
reverse1 = sorted(location)

reverse1.reverse()
print(reverse1)

location.reverse()
print(location)

location.reverse()
print(location)

location.sort()
print(location)

location.sort(reverse = True)
print(location)


'''Working with one of the programs from Exercises, use len() to print a message indicating the number of people you are
 inviting to dinner'''

Dinner = ['shehab', 'iqbal', 'nayeem', 'masum']
print(len(Dinner))