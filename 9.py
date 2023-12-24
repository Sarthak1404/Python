# class student 
# attributes name id grades 
# calculate average, student information
class Student:
    # constructor method to initialize the attributes
    def __init__(self, name, id, grades):
        self.name = name # string
        self.id = id # integer
        self.grades = grades # list of floats

    # method to calculate the average grades
    def average_grades(self):
        # use the built-in sum and len functions to compute the mean
        return sum(self.grades) / len(self.grades)

    # method to display student information
    def display_info(self):
        # use the print function to show the name, id, and average grades
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Average grades: {self.average_grades():.2f}")

# Create an object for the student class with some sample data
s1 = Student("A", 101, [90, 85, 95])
s2 = Student("B", 102,[100, 98, 95])

# Call the display_info method on the object
s1.display_info()
s2.display_info()
