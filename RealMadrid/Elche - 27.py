#Try/Except

try:
    answer = 20/0
    number = int(input("Enter your number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input!!!")
