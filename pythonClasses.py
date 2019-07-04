# class MyClass:
#     x=5
#     y=10;
#     z=20;
#     a=30;
# print(MyClass)
#
# myObj = MyClass()
#
# print(myObj.z)

class Person :
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def fullName(self):
        print(self.fname +" "+self.lname)
person2 = Person("Murali","Krishna")

# print(person2.fname)
person2.fullName()