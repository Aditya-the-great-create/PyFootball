#Exponential functions

def raise_to_the_power(base, power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(raise_to_the_power(7,3))

def SerieA(base, power):
    getafe = 1
    for Titles in range(power):
        getafe = getafe * base
    return getafe

print(SerieA(2,15))
