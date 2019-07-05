class Person:
    def __init__(self,email,age,contact):
        self.email = email;
        self.age = age;
        self.contact = contact
    def sayDetails(abc):
        print(abc.email)

person1 = Person("vmurali100@gmail.com",39,9663856625)

person1.email = "prabu@gmail.com"
del person1.email
# print(person1.email)
# print(person1.age)
# print(person1.contact)
person1.sayDetails()