numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
food_list = ['rice', 'yam', 'banana', 'beans', 'garri', 'bread', 'sugar', 'gas', 'tea', 'meat']

print(food_list)

ingredient = input('Enter a food')
for item in food_list:
    if item == ingredient:
        print(item, 'is in the list')

total = 0
for numbers in number:
    total = total + number