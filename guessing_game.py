#### version 1.1 ####

import random

class RandomNum:
    def __init__(self, random_number, player_choice, guess_tries):
        self.random_number = random_number
        self.player_choice = player_choice
        self.guess_tries = guess_tries

    def __repr__():
        print("This is a string for the class")

    @classmethod
    def generate_number(cls):
        return random.randint(1,10)
    
    @classmethod
    def get_guess_tries(cls):
        return 1

    @classmethod
    def get_player_choice(cls):
        player_choice = input("\nPlease enter your choice here: ")
        while True:
            try:
                player_choice = int(player_choice)
                break
            except ValueError:
                player_choice = input("Thats not a valid input. Please enter a number from 1 to 10: ")

        while player_choice <= 0 or player_choice >= 11:
            player_choice = input("That number is not from 1 and 10. Please enter your number again: ")
            while True:
                try:
                    player_choice = int(player_choice)
                    break
                except ValueError:
                    player_choice = input("Thats not a valid input. Please enter a number from 1 to 10: ")
        return player_choice  
        
    def guess_game(self):
        while self.guess_tries <= 3:
            if self.player_choice != self.random_number:
                self.guess_tries += 1
                if self.guess_tries == 4:
                    return print("\nSorry, all out of guesses.\nMy number was {}.\nPlay again real soon!\n".format(random_number))
                if self.guess_tries == 3:
                    print("\nSorry. You have one more try")
                    self.player_choice = self.get_player_choice()
                else:
                    print("\nSorry. Please try again. Guess again " + str(4 - self.guess_tries) + " more times")
                    self.player_choice = self.get_player_choice()
            else:
                return print("\nCongrats. You win!!! The number was:", self.random_number)


print("""
Its time for a super fun game. Everybody loves games =)
Im thinking of a number somewhere from 1 to 10. Which number am I thinking of?
I will give you three chances to pick the right number. Good luck!
""")
input("Press any key to start...")

guess_tries = RandomNum.get_guess_tries()
random_number = RandomNum.generate_number()
player_choice = RandomNum.get_player_choice()
guessingGame = RandomNum(random_number, player_choice, guess_tries)
guessingGame.guess_game()

##############################################


#### version 1.0 ####

#import random

#random_number = random.randint(1, 10)
#guess_tries = 1
#
#print("""
#Its time for a super fun game. Everybody loves games =)
#Im thinking of a number somewhere from 1 to 10. Which number am I thinking of?
#I will give you three chances to pick the right number. Good luck!
#""")
#
#
#while guess_tries <= 3:
#    player_choice = input("Please enter your choice here: ")
#
#    while True:
#        try:
#            player_choice = int(player_choice)
#            break
#        except ValueError:
#            player_choice = input("Thats not a valid input. Please enter a number from 1 to 10: ")
#
#    while player_choice <= 0 or player_choice >= 11:
#        player_choice = input("That number is not from 1 and 10. Please enter your number again: ")
#        while True:
#            try:
#                player_choice = int(player_choice)
#                break
#            except ValueError:
#                player_choice = input("Thats not a valid input. Please enter a number from 1 to 10: ")
#
#    if player_choice != random_number:
#        guess_tries += 1
#        if guess_tries == 4:
#            print("\nSorry, all out of guesses.\nMy number was {}.\nPlay again real soon!\n".format(random_number))
#            break
#        if guess_tries == 3:
#            print("Sorry. You have one more try")
#            continue 
#        else:
#            print("Sorry. Please try again. Guess again " + str(4 - guess_tries) + " more times")
#            continue
#    else:
#        print("Congrats. You win!!! The number was:", random_number)
#        break