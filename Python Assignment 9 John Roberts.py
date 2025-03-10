#Question 1
#This is a class made for defining a students' name, age, and grade.
'''This class is made using the init method and the details method, which allows the given parameters to be used
throughout the different methods via the use of 'self'.'''

print('Question 1 Results')

class Students:
    def __init__(self,name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade
    def details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Grade: ", self.grade)

student_1= Students("Raj", "16", "11th")
student_2= Students("Joe", "17", "11th")

student_1.details()
student_2.details()

#These are the results from using this class. It was remarkably straight forward once the structure of classes was
#explained in greater detail.

'''
Question 1 Results
Name:  Raj
Age:  16
Grade:  11th
Name:  Joe
Age:  17
Grade:  11th
'''

#Question 2
#This makes use of inheritance with Parent and Child classes through the use of the super() function.
'''This class is made using the init method and the super method, which is what essentially imports and inherits
the attributes that have already been defined from the Parent class of Staff.'''

print('Question 2 Results')

class Staff:
    def __init__(self,name, department, role, salary):
        self.name=name
        self.department=department
        self.role=role
        self.salary=salary

class Teacher(Staff):
    def __init__(self,name,department,role,salary,age):
        super().__init__(name,department,role,salary)
        self.age=age
    def details_staff(self):
        print("Name: ", self.name)
        print('Age: ', self.age)
        print("Role: ", self.role)
        print("Department: ", self.department)
        print('Salary: ', self.salary)

teacher_1=Teacher('Raj', 'Science', 'Teacher', '$60,000', '20')
teacher_2=Teacher('Joe', 'Science', 'Teacher', '$62,000', '58')

teacher_1.details_staff()
teacher_2.details_staff()

#This was an interesting change, as I did have to look up how to essentially import the information from the parent
#class in order for the inheritance to work. I also was unsure how this was any more useful than simply having teacher
#have those attributes written in as well, but then I realized that you can have this be done with any number of
#child classes and not have to redefine the attributes and parameters over and over again.
'''
Question 2 Results
Name:  Raj
Age:  20
Role:  Teacher
Department:  Science
Salary:  $60,000
Name:  Joe
Age:  58
Role:  Teacher
Department:  Science
Salary:  $62,000
'''

#Question 3
#This class is used for returning the square area and perimeter of two squares when given one side from each of them.
'''This class made use of the __init__ method as well as the details method to return the area and perimeter of a square
when given a length of one of the sides.'''

print('Question 3 Results')

class Square:
    def __init__(self, name, side1):
        self.side1=side1
        self.name=name
    def details_square(self):
        print("The Area of", self.name,  "is: ", int(self.side1) **2)
        print("The Perimeter of", self.name, " is: ", int(self.side1) * 4)


square1= Square('square1', '10')
square2= Square('square2', '20')

square1.details_square()
square2.details_square()

#Making this little class was fun, and it really shows how easy classes can make it to have a large amount of highly
#editable variables, which would be necessary when working with large amounts of data that fluctuates all the time.
'''Question 3 Results
The Area of square1 is:  100
The Perimeter of square1  is:  40
The Area of square2 is:  400
The Perimeter of square2  is:  80
'''