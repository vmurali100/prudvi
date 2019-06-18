friends = ("Murali","Krishna","Ram","Ravi")

print(friends[0])

for a in friends:
    if "Krishna" in friends:
        print("Murali Exist in in This Tuple")
        break
print(len(friends))

newFriends = tuple("Ram","Ravi","Murali","Kiran")

print(newFriends)