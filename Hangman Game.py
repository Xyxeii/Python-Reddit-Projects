##Readme
#create hangman figure
#add limbs as the user gets a letter wrong
#create a word bank
#print word at the end if the user loses
#add a give up option

import random
import math
import time

class hm_game():
    def __init__(self):
        print("\n#########################\n## Welcome to Hangman! ##\n#########################")
        print("In this game you start by choosing a category. You'll then be given a word to guess related to that category.\nYou guess one letter of the word at a time and each time you guess a letter incorrectly, your character will be that much closer to being hung!\nFirst lets start with your name so we can track your score!\n")
        self.user_name = input("What would you like me to call you? ").title()
        print("\nThat's an interesting name.\nWelcome {}!\n".format(self.user_name))

        self.score = Calc_Points()
        
        while True:
            self.begin = input("Are you ready to play? (y/n) ")
            if self.begin[0].lower() == 'y':
                self.new_game()
                break
            elif self.begin[0].lower() == 'n':
                print("Okay. Goodbye {}.".format(self.user_name))
                return
            else:
                print("I'm sorry, I don't understand.")
        
    def new_game(self):
        hang_man_display = ["________\n|      |\n|       \n|\n|\n|\n|_______",
        "________\n|      |\n|      O\n|\n|\n|\n|_______",
        "________\n|      |\n|      O\n|      |\n|\n|\n|_______",
        "________\n|      |\n|      O\n|     /|\n|\n|\n|_______",
        "________\n|      |\n|      O\n|     /|\ \n|      |\n|\n|_______",
        "________\n|      |\n|      O\n|     /|\ \n|      |\n|     /\n|_______",
        "________\n|      |\n|      O\n|     /|\ \n|      |\n|     / \ \n|_______",
        "________\n|      |\n|      O\n|     /|\ \n|      |\n|    _/ \ \n|\n|_______",
        "________\n|      |\n|      O\n|     /|\ \n|      |\n|    _/ \_\n|\n|_______"
    ]

        abc = 'abcdefghijklmnopqrstuvqxyz'
        get_word = self.word_gen()
        word = ['_' if x.lower() in abc else x for x in get_word]
        guesses_remaining = 9
        count = 0
        used_letters = ""
        print("\nGood luck!\nAt any point you can type \"quit\" to exit the game.\n{}\n{}".format(hang_man_display[count], " ".join(word)))
        while guesses_remaining > 0:
            letter_input = input("\nGuess a letter: ")
            if len(letter_input) == 1:
                if letter_input in used_letters:
                    print("Oops, you already picked that letter. Try again!")
                else:
                    used_letters += letter_input
                    if letter_input in get_word.lower():
                        for i, n in enumerate(get_word.lower()):
                            if n == letter_input:
                                self.score.add_points(letter_input)
                                word[i] = letter_input
                        if "".join(word) == get_word.lower():
                            print("\n{}\nCongratulations, you win!\n\nThe word was: {}".format(hang_man_display[count], "".join(word).title()))
                            self.score.total_points("".join(word), guesses_remaining)
                            break
                        else:
                            print("That's correct!")
                        time.sleep(1)
                    else:
                        print("Sorry that's incorrect :( Try again.")
                        count += 1
                        guesses_remaining -= 1
                        time.sleep(1)
                        if guesses_remaining == 0:
                            print("\n________\n|      |\n|      Q\n|     /|\ \n|      |\n|    _/ \_\n|\n|_______\nGAME OVER\n\nThe word was:\n{}".format(get_word))
                            break
                    print("\n{}\n{}".format(hang_man_display[count], " ".join(word)))
            elif letter_input.lower() == "quit":
                print("Okay. Goodbye {}.".format(self.user_name))
                return
            elif letter_input.lower() == get_word.lower():
                print("\n{}\nCongratulations, you win!\n\nThe word was: {}".format(hang_man_display[count], get_word.title()))
                self.score.total_points("".join(word), guesses_remaining)
                break
            else:
                print("Only one letter please :)")
        print("{name} your current score is {score}: ".format(name = self.user_name, score = self.score))
        play_again = input("\nWould you like to play again? (y/n) ")
        while True:
            if play_again[0].lower() == 'y':
                self.new_game()
                break
            elif play_again[0].lower() == 'n':
                print("{name} you finished with a score of: {score}.".format(name = self.user_name, score = self.score))
                return
            else:
                print("I'm sorry, I don't understand.")

    def word_gen(self):
        category_list = {'Cars':['cruiser', 'Jeep', 'hybrid', 'Tesla', 'limousine', 'taxi cab'], 'Country Names':['Canada', 'Costa Rica', 'Denmark', 'Guatemala', 'South Korea', 'Portugal', 'Madagascar'], 'Elements':['Cadmium', 'Calcium', 'Hydrogen', 'Magnesium', 'Mercury', 'Promethium'], 'Food':['acorn squash', 'black-eyed peas', 'cayenne pepper', 'cheesecake', 'donuts', 'french fries', 'poutine'], 'Instruments':['acoustic guitar', 'bongo drum', 'flugelhorn', 'harmonica', 'slide whistle'], 'Sports':['baseball', 'hockey', 'shuffleboard', 'curling', 'nascar', 'drag racing', 'cross country', 'horseshoes', 'Olympics']}
        print("\nHere is your list of categories: {}".format(", ".join([*category_list.keys()])))
        while True:
            user_input = input("Which category would you like choose? ").title()
            if user_input in category_list.keys():
                print("\nYou've chosen {}!".format(user_input))
                return random.choice(category_list[user_input])
            else:
                print("I'm sorry, that's not a valid category")

class Calc_Points():
    def __init__(self):
        self.temp_points = 0
        self.point_total = 0

    def __repr__(self):
        return repr(self.point_total)

    def add_points(self, characters):
        abc = 'abcdefghijklmnopqrstuvqxyz'
        vowels = 'aeiou'
        consonants = set(abc) - set(vowels)

        for c in characters:
            if c in vowels:
                self.temp_points += 10
            elif c in consonants:
                self.temp_points += 30
            elif c == " ":
                self.temp_points += 20

    def total_points(self, word, guesses_remaining):
        if " " in word:
            self.temp_points += word.count(" ") * 20
        self.temp_points += guesses_remaining * 50
        self.point_total += self.temp_points
        self.temp_points = 0
        return self.point_total

if __name__ == "__main__":
   game_1 = hm_game()