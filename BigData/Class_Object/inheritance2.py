from inheritance import Person
class Student(Person):
  def __init__(self, fname, lname):
    """
    To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
    """
    # Person.__init__(fname, lname)
    """
    Python also has a super() function that will make 
    the child class inherit all the methods and properties from its parent.
    By using the super() function, you do not have to use the name of the parent element, 
    it will automatically inherit the methods and properties from its parent
    """
    super().__init__(fname, lname)
    
s = Student("Mario", "Rossi")
s.printname()