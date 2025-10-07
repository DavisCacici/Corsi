"""
In your method you could add new property and method 
"""

from inheritance import Person
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)
        
s = Student("Pino", "Daniele", 2004)
print(s.graduation_year)
s.welcome()