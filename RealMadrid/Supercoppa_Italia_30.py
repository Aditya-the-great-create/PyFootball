#Importing Modules

#For installing libraries: pip install library_name
#For uninstalling libraries: pip uninstall library_name

import random

trophies_in_ucl = 15
winners_in_laliga = 36
real_madrid = ["Kylian Mbappe", "Vini Jr.", "Jude Belligham", "Valverde", "Gonzalo Garcia"]

def coppa_italia(teams):
    return random.randint(1, teams)

def saudi_pro_league(players):
    return players[players.index("Cristiano Ronaldo") + 1]

def roll_dice(num):
    return random.randint(1, num)



