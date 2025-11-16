#Guessing Game

secret_word = "Ronaldo"
guess = ""
guess_count = 0
guess_limit = 3
out_of_the_guesses = False

while guess != secret_word and not(out_of_the_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the word:")
        guess_count += 1
    else:
        out_of_the_guesses = True

if out_of_the_guesses:
    print("You Lose! Keep going!")
else:
    print("You win!")

unique_word = "Luis Suarez"
guess = ""
guess_count = 0
guess_limit = 5
no_guesses = False

while guess != unique_word and not(no_guesses):
    if guess_count < guess_limit:
        guess = input("Enter the word please: ")
        guess_count += 1
    else:
        no_guesses = True

if no_guesses:
    print("You Lose! Try Again!")
else:
    print("You win!")
