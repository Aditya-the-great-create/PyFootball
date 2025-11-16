num1 = int(input("Enter the first number: "))
op = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print("Invalid Operator")

leg1 = int(input("Enter Leg1 score: "))
leg2 = int(input("Enter Leg2 score: "))

if leg1 == leg2:
    penalties1 = int(input("Enter Penalties of Team 1: "))
    penalties2 = int(input("Enter Penalties of Team 2: "))
    if penalties1 >= penalties2:
        print("Winner: Team 1")
    else:
        print("Winner: Team 2")
else:
    print(leg1 + leg2)