import math
import os


global_id = 1
class Shape:
    def __init__(self):
        global global_id
        self._id = global_id
        global_id += 1

    @property
    def id(self):
        return self._id

    def print(self):
        print(f"ID: {self.id}, Name: {self.__class__.__name__}, Perimeter: {self.perimeter()}, Area: {self.area()}")

    def perimeter(self):
        return None

    def area(self):
        return None


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi

    def print(self):
        print(f"ID: {self.id}, Name: {self.__class__.__name__}, Perimeter: {self.perimeter()}, Area: {self.area()}")


class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.semi_major = max(a, b)
        self.semi_minor = min(a, b)

    def area(self):
        return math.pi * self.semi_major * self.semi_minor

    def eccentricity(self):
        try:
            return math.sqrt((self.semi_major ** 2) - (self.semi_minor ** 2))
        except ValueError:
            return None

    def print(self):
        print(f"ID: {self.id}, Name: {self.__class__.__name__}, Perimeter: {self.perimeter()}, Area: {self.area()}, "
              f"Linear eccentricity: {self.eccentricity()}")


class Rhombus(Shape):
    def __init__(self, diagonal_one, diagonal_two):
        super().__init__()
        self.diagonal_two = diagonal_two
        self.diagonal_one = diagonal_one

    def perimeter(self):
        return 4 * math.sqrt((self.diagonal_one / 2) ** 2 + (self.diagonal_two / 2) ** 2)

    def area(self):
        return (self.diagonal_one * self.diagonal_two) / 2

    def side(self):
        return math.sqrt((self.diagonal_one / 2) ** 2 + (self.diagonal_two / 2) ** 2)

    def inradius(self):
        try:
            return (self.diagonal_one * self.diagonal_two) / (
                    4 * math.sqrt((self.diagonal_one ** 2 + self.diagonal_two ** 2)))
        except ZeroDivisionError:
            return None

    def print(self):
        print(f"ID: {self.id}, Name: {self.__class__.__name__}, Perimeter: {self.perimeter()}, Area: {self.area()}, "
              f"side: {self.side()}, in-radius: {self.inradius()}")

    ################################## Function #######################################


shapes_list = []  # This will store the shapes in memory


def load_file(file_name):
    if not os.path.exists(file_name):
        print(f"File '{file_name}' does not exist.")
        return
    else:
        with open(file_name) as file:
            row_counter = 0
            errors_counter = 0
            global shapes_list
            shapes_list = file.read().splitlines()
            print(f"\nThe file '{file_name}' is being processed!")
            for line in shapes_list:
                row_counter += 1
                words = line.split()
                word = words[1:]
                for x in word:
                    if int(x) < 0:
                        errors_counter += 1
                        shapes_list.remove(line)
                        print(f"Error: Invalid {words[0]} on line {row_counter}: {line}")
            print(
                f"Processed {row_counter} row(s), {row_counter - errors_counter} shape(s) added, {errors_counter} error(s)")
            print("here's the added shapes")
            for line in shapes_list:
                print(line)


def toset(list_object):
    if len(list_object) == 0:
        print("\nYou have passed an empty list! Nothing will be set!")
    else:
        global shapes_list
        shapes_list = list(set(list_object))  # Assuming each shape class has a __hash__ method
        print(f"\nRemoved duplicates. {len(shapes_list)} unique shapes remaining.")
        for line in shapes_list:
            print(line)


def save_file(file_name, list_object):
    if len(list_object) == 0:
        print("You have passed an empty list! Nothing will be saved!")
    else:
        with open(file_name, "w") as file:
            for element in list_object:
                file.write(element + "\n")


def print_fun(list_object):
    global shapes_list
    shapes_list = list_object
    shapes = []
    for line in shapes_list:
        line = line.strip().lower()
        if line:
            parts = line.split()
            if parts[0] == 'shape':
                shapes.append(Shape())
            elif parts[0] == 'rhombus':
                try:
                    diagonal_one = float(parts[1])
                    diagonal_two = float(parts[2])
                    shapes.append(Rhombus(diagonal_one, diagonal_two))
                except (ValueError, IndexError):
                    print("Invalid Rhombus parameters")
            elif parts[0] == 'circle':
                try:
                    radius = float(parts[1])
                    shapes.append(Circle(radius))
                except (ValueError, IndexError):
                    print("Invalid Circle parameters")
            elif parts[0] == 'ellipse':
                try:
                    a = float(parts[1])
                    b = float(parts[2])
                    if a >= 0 and b >= 0:
                        shapes.append(Ellipse(a, b))
                    else:
                        print("Invalid Ellipse parameters, dimensions must be non-negative")
                except (ValueError, IndexError):
                    print("Invalid Ellipse parameters")

    # Print shapes
    for shape in shapes:
        shape.print()


def summary():
    global shapes_list
    dictionary_object = dict()
    shape_counter = 0
    for line in shapes_list:
        words = line.split()
        word = words[0]
        if word in dictionary_object:
            dictionary_object[word] += 1
            shape_counter += 1
        else:
            dictionary_object[word] = 1
            shape_counter += 1
    sorted_object = sorted(dictionary_object.keys())
    for key in sorted_object:
        if key == "shape":
            print(f"{key}: {shape_counter}")
        else:
            value = dictionary_object.get(key)
            print(f"{key}: {value}")


def details():
    for shape in shapes_list:
        print(shape)


t = True
while t:
    print('''
                 Manu
Please choose from the following options: 
    - LOAD: loads a database of shapes.
    - TOSET: converts the current multi-set in memory to a set (removes duplicates).
    - SAVE: saves the current in-memory database to a file.
    - PRINT: prints the current in-memory database to the standard output.
    - SUMMARY: prints the summary of the in-memory database to the standard output.
    - DETAILS: prints the detailed information of the in-memory database objects to the standard output.                         
    - QUIT: terminate the program
''')

    choice = str(input("please enter your choice: ")).strip().lower()
    if choice == "load":
        file_name = str(input("please enter your database file (make sure the file existed): "))
        load_file(file_name)


    elif choice == "toset":
        toset(shapes_list)


    elif choice == "save":
        file_name = str(input("please enter your updated_database file name you with to save the new data at: "))
        save_file(file_name, shapes_list)


    elif choice == "print":
        print_fun(shapes_list)


    elif choice == "summary":
        summary()


    elif choice == "details":
        details()


    elif choice == "quit":
        print("the programme will be terminated! Thank you for participating! ")
        t = False


    else:
        print("You have not entered a valid choice. The programme will be terminated!")
