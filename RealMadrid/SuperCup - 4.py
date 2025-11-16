#Strings
#\ is used for escape statement in between Strings. Run the below code (Line 3).
print("King\"England")
print("King\England")

phrase = "King England"
print(phrase + " is good")

print(phrase.lower())
print(phrase.upper())

print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))

print(phrase[3])
print(phrase.index("Eng"))
print(phrase.replace("King", "Queen"))