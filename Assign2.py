#Question:1::define a python class Person with instance object variables name and age Set instance object variables in _init()_ method Also define show() method to display name and age of a person 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage:
# Creating an instance of the Person class
person1 = Person("John Doe", 25)

# Displaying the information using the show() method
person1.show()


##Question:2::Define a class Circle With instance object variable radius Provide setter and getter for radius Also define getArea() and getCircumfrence methods
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using _radius to indicate it as a protected variable

    # Getter method for radius
    def get_radius(self):
        return self._radius

    # Setter method for radius
    def set_radius(self, radius):
        if radius < 0:
            print("Radius cannot be negative. Setting radius to 0.")
            self._radius = 0
        else:
            self._radius = radius

    # Method to calculate and return the area of the circle
    def get_area(self):
        return math.pi * self._radius ** 2

    # Method to calculate and return the circumference of the circle
    def get_circumference(self):
        return 2 * math.pi * self._radius

##Question:3::Define a class Rectangle with length and breath as instance object variables provide setDimensions()show Dimensions() and getArea() method in it 
class Rectangle:
    def __init__(self, length, breadth):
        self._length = length  # Using _length to indicate it as a protected variable
        self._breadth = breadth  # Using _breadth to indicate it as a protected variable

    # Method to set the dimensions of the rectangle
    def set_dimensions(self, length, breadth):
        if length < 0 or breadth < 0:
            print("Dimensions cannot be negative. Setting dimensions to 0.")
            self._length = 0
            self._breadth = 0
        else:
            self._length = length
            self._breadth = breadth

    # Method to display the dimensions of the rectangle
    def show_dimensions(self):
        print(f"Length: {self._length}, Breadth: {self._breadth}")

    # Method to calculate and return the area of the rectangle
    def get_area(self):
        return self._length * self._breadth

# Example usage:
# Creating an instance of the Rectangle class
class Rectangle:
    def __init__(self, length, breadth):
        self._length = length  # Using _length to indicate it as a protected variable
        self._breadth = breadth  # Using _breadth to indicate it as a protected variable

    # Method to set the dimensions of the rectangle
    def set_dimensions(self, length, breadth):
        if length < 0 or breadth < 0:
            print("Dimensions cannot be negative. Setting dimensions to 0.")
            self._length = 0
            self._breadth = 0
        else:
            self._length = length
            self._breadth = breadth

    # Method to display the dimensions of the rectangle
    def show_dimensions(self):
        print(f"Length: {self._length}, Breadth: {self._breadth}")

    # Method to calculate and return the area of the rectangle
    def get_area(self):
        return self._length * self._breadth

# Example usage:
# Creating an instance of the Rectangle class
rectangle1 = Rectangle(5, 7)

# Displaying the initial dimensions
rectangle1.show_dimensions()

# Setting new dimensions using set_dimensions method
rectangle1.set_dimensions(8, 10)

# Displaying the updated dimensions
rectangle1.show_dimensions()

# Calculating and displaying the area of the rectangle
print(f"Area of the Rectangle: {rectangle1.get_area()}")



#Question:4::Define a class Book with instance object variables bookid , title and price Initilise them via _init_() method Also define method to show book variables
class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def show_book_details(self):
        print(f"Book ID: {self.bookid}")
        print(f"Title: {self.title}")
        print(f"Price: ${self.price:.2f}")

# Example usage:
# Creating an instance of the Book class
book1 = Book(bookid=1, title="The Great Gatsby", price=15.99)

# Displaying the book details using the show_book_details method
book1.show_book_details()


##Question:5::Define a class Team with instanse object variable a list of  team member names Provide methods to input member names and display member names
class Team:
    def __init__(self):
        self.team_members = []  # Initializing an empty list for team members

    def input_member_names(self):
        num_members = int(input("Enter the number of team members: "))
        for i in range(num_members):
            member_name = input(f"Enter name of team member {i + 1}: ")
            self.team_members.append(member_name)

    def display_member_names(self):
        if not self.team_members:
            print("No team members to display.")
        else:
            print("Team Members:")
            for member_name in self.team_members:
                print(member_name)

# Example usage:
# Creating an instance of the Team class
team1 = Team()

# Inputting team member names
team1.input_member_names()

# Displaying team member names
team1.display_member_names()
