#if statement and Boolean statement
from Supercoppa_Italia_30 import real_madrid

is_fcbarcelona = True
is_como = False

if is_fcbarcelona and is_como:
    print("Both are Winners of 2025 season")
elif is_fcbarcelona and not(is_como):
    print("FC Barcelona are the winners")
elif not(is_fcbarcelona) and is_como:
    print("Como are the winners.")
else:
    print("Draw of 2025 season")

#if is_fcbarcelona or is_como:
#    print("Both are the winners of 2025 season. ")
#else:
#   print("Draw of 2025 season")

real_madrid = False
fcbarcelona = True
if not(real_madrid) and fcbarcelona:
    print("FC Barcelona winner")
elif real_madrid and not(fcbarcelona):
    print("Real Madrid winner")
else:
    print("Draw")

