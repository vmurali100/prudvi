# Creating A function
def sayHello():
    print("Hello I am from Funtions")

# Calling a Function
# sayHello()

# Passing a Arguments
def payFees(amt):
    print("Amount Paid : ")
    print(amt)
# payFees(10000)

def fullName(fname,lname):
    print("Your Full Name is "+fname +" "+lname)
# fullName("Murali","Krishna") 

def aboutme(country="India"):
    print("I am from "+country)

aboutme("America")
aboutme()