#List Functions

jersey_numbers = [24, 24, 10, 23, 9]
friends = ["Cole", "James", "Luke", "Lionel", "Luke", "Erling"]
#friends.extend(jersey_numbers)
#friends.insert(2, "Cristiano")
#friends.append("Achraf")
#jersey_numbers.append(2)
#friends.remove("Luke")

#friends.clear()
print(friends.index("Lionel"))
print(friends.count("Luke"))
jersey_numbers.sort()
jersey_numbers.reverse()

friends2 = friends.copy()
print(friends2)
