print('''
For distance press A
For force press B
For displacement press C
For perimeter_of_rectangle press D
For momentum press E
''')

def calculate_distance():
    speed = float(input('Enter speed: '))
    time = float(input('Enter time: '))
    distance = speed * time
    print(f"Distance: {distance} units")

def calculate_force():
    mass = float(input('Enter mass: '))
    acceleration = float(input('Enter acceleration: '))
    force = mass * acceleration
    print(f"Force: {force} Newtons")

def calculate_displacement():
    velocity = float(input('Enter velocity: '))
    time = float(input('Enter time: '))
    displacement = velocity * time
    print(f"Displacement: {displacement} units")

def calculate_perimeter_of_rectangle():
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    perimeter = 2 * (length + width)
    print(f"Perimeter of rectangle: {perimeter} units")

def calculate_momentum():
    mass = float(input('Enter mass: '))
    velocity = float(input('Enter velocity: '))
    momentum = mass * velocity
    print(f"Momentum:{momentum} kg·m/s")

choice = input("What do you need (A/B/C/D/E)? ").strip().upper()

if choice == 'A':
    calculate_distance()
elif choice == 'B':
    calculate_force()
elif choice == 'C':
    calculate_displacement()
elif choice == 'D':
    calculate_perimeter_of_rectangle()
elif choice == 'E':
    calculate_momentum()
else:
    print('Invalid choice. Please enter an alphabet between A to E')
