"""
guessing game
by: Joseph Howly
A little game of trying to guess a number from 0-100 randomly chosen b the computer
On 15-9-26
"""

#Imports

import random

#Variables
play = True
computer_guess = random.randint(0, 100)
nb_guessed = 0


#The game...
def game():

    global computer_guess, play, nb_guessed


    try:
        player_guess = int(input("Choisi un nombre entre 1 et 100: "))
    except:
        exit("Pas de lettres buddy.")


    if computer_guess == player_guess:
        print("Tu l'as bien eu!")
        nb_guessed += 1
        print(f"Tu l'as eu en {nb_guessed} essaies.")
        retry = input("Veut-tu rejouer? (y/n): ")

        if retry == "y":
            nb_guessed = 0
            print("J'ai rechoisi un nombre.")
            computer_guess = random.randint(0, 100)
            game()

        elif retry == "n":
            print("Merci pour avoir jouer!")
            play = False

        else:
            exit("C'est quoi ça?")

    else:
        if computer_guess < player_guess:
            print("Tu as devenu trop haut.")
            nb_guessed += 1

        else:
            print("Tu as devenu trop bas.")
            nb_guessed += 1


print("J'ai choisi un nombre entre 1 et 100.")






#Calling the game
while play:
    game()