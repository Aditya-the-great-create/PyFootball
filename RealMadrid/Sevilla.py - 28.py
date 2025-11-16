#Reading a file

supercup_file = open("Supercup.txt", "r")
#supercup_file = open("Supercup.txt", "w")

#print(supercup_file.readable())

#print(supercup_file.read())

#print(supercup_file.readline())
#print(supercup_file.readline())
#print(supercup_file.readline())
#print(supercup_file.readlines()[3])

for teams in supercup_file.readlines():
    print(teams)

supercup_file.close()