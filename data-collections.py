# Lists
# Tuple
# Set
# Disctionary

# List
friends = ["Murali","Krishna","Pridvi","Ram"]
# print(friends[2])
# friends[0] = "Murali Krishna"
# print(friends[0])

# Looping through all its in List
# for a in friends:
#     print(a)

# Checking value is exist or not in the list
# if "Mural" in friends:
#     print("Yes Murali Is exist in The list")

#adding a Value to the Lasy of the List
# friends.append("VMR")# will add a value to the last of the list
# friends.insert(1,"VVVM") # insert An Element in Specified Index
#print(friends.pop())#remove the last Element in list

# del friends[2]
# friends.pop(2)

# del friends // will remove the entire list
# friends.clear()

# myFriends = friends.copy()
myFriends = list(friends)
print(myFriends)
# friends.remove("VMR")
for a in friends:
    print(a)

# Total length of list
print(len(friends))