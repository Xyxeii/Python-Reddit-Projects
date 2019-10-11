##README
#after every guess the user is told if his guess what higher or lower then the answer
#when the user guesses correctly, print a congratz message

#add intro message
#store and display the amount of guesses used *enumerate
#allow a 'play again' option

import random
import math

class hl_game():
    def __init__(self):
        print("Welcome to the Higher-Lower Guessing Game!\n")
        print("In this game you'll have 10 chances to guess a number between 1-100!\nEach time you guess incorrectly, you'll be told whether your next guess should be \"higher\" or \"lower\". First lets start with your name!\n")
        self.user_name = input("What would you like me to call you? ").title()
        print("\nThat's an interesting name.\nWelcome {}!\n".format(self.user_name))
        
        while True:
            self.begin = input("Are you ready to play? (y/n) ")
            if self.begin[0].lower() == 'y':
                self.new_game()
                break
            elif self.begin[0].lower() == 'n':
                print("Okay. Goodbye {}.".format(self.user_name))
                break
            else:
                print("I'm sorry, I don't understand.")
        
    def new_game(self):
        self.max_attempts = 10
        self.current_attempts = self.max_attempts
        self.secret_number = random.randint(0, 100)
        ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(math.floor(n/10)%10!=1)*(n%10<4)*n%10::4])
        print("Good luck! You have {current} / {max} guesses.\n".format(current=self.current_attempts, max=self.max_attempts))
        for guess_number in range(1, self.max_attempts + 1):
            try:
                user_guess = int(input("What is your {} guess? ".format(ordinal(guess_number))))
                print("")
                if user_guess == self.secret_number:
                    print("\nCongratulations! The number was {}.\nYou guessed correctly with {} guesses remaining!".format(self.secret_number, self.max_attempts - guess_number))
                    break
                else:
                    up_or_down = "higher!" if self.secret_number > user_guess else "lower!"
                    print("I'm sorry, that was incorrect. Try guessing {}".format(up_or_down))
            except ValueError:
                print("That is not a correct number value")
        if guess_number == self.max_attempts:
            print("Game Over :( The number to guess was {}. Better luck next time!".format(self.secret_number))
        play_again = input("\nWould you like to play again? (y/n) ")
        while True:
            if play_again[0].lower() == 'y':
                self.new_game()
                break
            elif play_again[0].lower() == 'n':
                print("Okay. Goodbye {}.".format(self.user_name))
                break
            else:
                print("I'm sorry, I don't understand.")


if __name__ == "__main__":
    game_1 = hl_game()