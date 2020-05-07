#4.10

pizzas = ['Tuna', 'Italian', 'Greek', 'French', 'Beefish']
Animals = ['Cat', 'Cow', 'Lamb', 'Hen']

print(pizzas[0:3])
print(pizzas[2:3])
print(pizzas[-3:])

#4.11

Friend_pizza = pizzas[:]

pizzas.append('Redish')
Friend_pizza.append('Blakish')

print(pizzas)
print(Friend_pizza)

#4.12

for pizza in pizzas:
    print(pizza)

for friend_pizza in Friend_pizza:
    print(friend_pizza)