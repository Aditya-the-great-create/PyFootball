#If Statement + Function
from Supercoppa_Italia_30 import real_madrid


def CopaDelRey(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(CopaDelRey(39, 393, 777))

def SupercopaDeEspana(semi_final_1, semi_final_2, final):
    if semi_final_1 >= semi_final_2:
        return semi_final_1 and final
    else:
        return semi_final_2


print(SupercopaDeEspana("real_madrid", "athletic_lub", "real_madrid"))


