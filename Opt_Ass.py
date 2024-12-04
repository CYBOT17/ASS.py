Price_list = [800, 700, 600, 500, 400, 300, 200, 100]

reversed_numbers = []

for i in range(len(Price_list) - 1, -1, -1):
    reversed_numbers.append(Price_list[i])

print("Original list:", Price_list)
print("Reversed list:", reversed_numbers)
