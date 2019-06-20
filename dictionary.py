person = {
    "fname":"Murali",
    "lname":"Krishna",
    "email":"vmurali100@gmail.com"
}
print(person)
# print(person['fname'])
#
# newName = person.get('fname')
# print(newName)
# person['email'] = "muralikrishna@gmail.com"
#
# print(person)

# for a in person:
#     print(person[a])

# for a in person.values():
#     print(a)

# for x,y in person.items():
#     print(x,y)

# if "fname" in person:
#     print("Yes , Fname is Exist")

person['age'] = 39;

person.pop('age')

person.popitem()

# person.clear()
# person2 = person.copy()
# person2 = dict(person)
# print(person2)

print(person)

print(len(person))
