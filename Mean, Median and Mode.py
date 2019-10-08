##Create 3 total functions for mean, median, mode

##Mean
#allow the user to choose the amount of decimal places

##Median
# return 2 numbers if the list is even

##Mode
# if there are multiple modes, return all of them

## Create a wrapper function for user input

class Moct():
    def __init__(self):
        while True:
            try:
                self.user_input = input("Please enter your numbers separated by spaces: ").split()
                self.numbers = (float(i) for i in self.user_input)
                break
            except:
                print("I'm sorry, you entered an invalid number.\n")
        
        self.list_length = len(self.user_input)

    def __repr__(self):
        return "These are your numbers: {}".format(", ".join(self.user_input))

    def get_mean(self):
        while True:
            try:
                decimal_places = int(input("To how many decimal places would you like? "))
                break
            except:
                print("I'm sorry you entered an invalid number.\n")
        if decimal_places > 0:
            return "\nMean is: {}".format(round(sum(self.numbers) / self.list_length, decimal_places))
        else:
            return "\nMean is: {}".format(sum(self.numbers) / self.list_length)




    def get_median(self):
        sorted_input = self.user_input.sort()
        if self.list_length % 2 == 0:
            return "Median is: {} & {}".format(sorted_input[int((self.list_length / 2) - 0.5)], sorted_input[int((self.list_length / 2) + 0.5)])
        else:
            return "Median is: {}".format(sorted_input[int(self.list_length / 2)])


    def get_mode(self):
        count_occ = {}
        highest_count = 1
        mode = []
        for number in self.user_input:
            try:
                count_occ[number] += 1
                if count_occ[number] > highest_count:
                    highest_count = count_occ[number]
            except:
                count_occ[number] = 1
        for key, value in count_occ.items():
            if value == highest_count:
                mode.append(key)
        if len(mode) > 1:
            return "Your modes are: {} ".format(", ".join(mode))
        else:
            return "Your mode is: {} ".format("".join(mode))


if __name__ == "__main__":
    numbers_set_1 = Moct()
    print(numbers_set_1)
    print(numbers_set_1.get_mean())