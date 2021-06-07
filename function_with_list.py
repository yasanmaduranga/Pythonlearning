
food =["cake","ice-cream","watalappan","jeli"]

food.insert(2,"custed")

price =[12,13,14,15,16]

print(food)

food.extend(price)

print(food)

print(food.index("cake"))

print(food.count("cake"))

random = food.copy() + price.copy()
print(random)