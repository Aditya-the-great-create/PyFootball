#MCQ
#You have a box (topthree) full of small envelopes (top), each with a name inside (fifaplayeroftheyear).
#If you want to check the name in one envelope, you open that envelope (top), not the whole box (topthree).

from AC_Monaco_35 import Winners

nominations = [
    "France:\n (a) Mbappe\n (b) Dembele\n (c) Benzema\n (d) Mendes\n",
    "Portugal\n: (a) Cristiano Ronaldo\n (b) Feranandes\n (c) Mendes\n",
    "Argentina\n: (a) Martinez\n (b) Messi\n (c) Palacios\n"
]


topthree = [
    Winners(nominations[0], "a"),
    Winners(nominations[1], "a"),
    Winners(nominations[2], "b"),
]

def run_test(topthree):
    score = 0
    for greatest in topthree:
        fifaplayeroftheyear = input(greatest.ballondor)
        if fifaplayeroftheyear == greatest.fifaplayeroftheyear:
            score += 1
    print("You got " + str(score) + "/" + str(len(topthree)) + " correct")

run_test(topthree)




