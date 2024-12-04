print('''

for distance press A

for force press B

for displacement press C

for perimeter_of_rectangle press D

for momentum press E ''')

def calculate_distance():
    speed = float(input('Enter speed'))
    time = float(input('Enter time'))
    distance = speed * time
    print(distance)
calculate_distance()

def calculate_force():
    mass = float(input('Enter mass'))
    acceleration = float(input('Enter acceleration'))
    force = mass * acceleration
    print(force)
calculate_force()

def calculate_displacement():
    velocity = float(input('Enter Velocity'))
    time = float(input('Enter time'))
    displacement = velocity * time
    print(displacement)
calculate_displacement()

def calculate_perimeter_of_rectangle():
    length = float(input('Enter Length'))
    width = float(input('Enter width'))
    perimeter_of_rectangle = length + width
    print(perimeter_of_rectangle)
calculate_perimeter_of_rectangle()

def calculate_momentum():
    mass = float(input('Enter mass'))
    velocity = float(input('Enter velocity'))
    momentum = mass * velocity
    print(momentum)
calculate_momentum()

choice= 'What do you need'
if choice== 'A' or choice == 'a':
    calculate_distance()
elif choice== 'B' or choice == 'b':
    calculate_force()
elif choice== 'C' or choice == 'c':
    calculate_displacement()
elif choice== 'D' or choice == 'd':
    calculate_perimeter_of_rectangle()
elif choice== 'E' or choice == 'e':
    calculate_momentum()

else: print('Invalid choice. Please enter an alphabet between A to E')

