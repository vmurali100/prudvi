class Person:
    def __init__(self,fname,lname):
        self.fname=fname;
        self.lname=lname
    def printFullName(self):
        print(self.fname +" "+self.lname)

class Student(Person):
    pass

student1 = Student("Prabu","Kumar")

student1.printFullName()