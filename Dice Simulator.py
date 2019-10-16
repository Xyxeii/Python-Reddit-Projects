import random

class Dice_Sim(int):
    def __init__(self, dice_roll):
        self.dice_roll = dice_roll

    def display_dice(self):
        edge = "+-------+"
        row_1 = "|   O   |"
        row_2 = "| O     |"
        row_3 = "| O   O |"
        blank = "|       |"
        print_row_1 = blank if self.dice_roll == 1 else row_3 if self.dice_roll >= 4 else row_2[::-1]
        print_row_2 = row_3 if self.dice_roll == 6 else row_1 if self.dice_roll % 2 != 0 else blank
        print_row_3 = blank if self.dice_roll == 1 else row_3 if self.dice_roll >= 4 else row_2
        return f"{edge}\n{print_row_1}\n{print_row_2}\n{print_row_3}\n{edge}"

def roll_dice():
    while True:
        try:
            amount_of_dice = int(input("How many dice do you want to roll? "))
            dice_roll_list = []
            for dice in range(0, amount_of_dice):
                dice = Dice_Sim(random.randint(1, 6))
                print(dice.display_dice())
                dice_roll_list.append(int(dice))
            return f'You rolled a {", ".join(map(str, dice_roll_list))} and your total is {sum(dice_roll_list)}'
        except:
            print("Sorry that's not a valid number")


if __name__ == '__main__':
    while True:
        print(roll_dice())
        roll_again = input("\nWould you like to roll again? (y/n) ")
        if roll_again[0].lower() == 'y':
            continue
        elif roll_again[0].lower() == 'n':
            break
        else:
            print("I'm sorry I don't understand? ")

