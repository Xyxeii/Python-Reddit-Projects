import time

def triple_checker(input_list):
    c = max(input_list)
    input_list.pop(input_list.index(max(input_list)))
    a, b = input_list
    if a**2 + b**2 == c**2:
        return "This is a Pythagorean Triple!"
    else:
        return "This is not a Pythagorean Triple."

def input_handler():
    user_input_list = []
    for side_number in range(1,4):
        user_input = input("Please enter side #{}: ".format(side_number))
        while user_input.isdigit() == False:
            print("Error: That was not a correct number value")
            user_input = input("Please enter a correct value for side #{}: ".format(side_number))
        else:
            user_input_list.append(int(user_input))
    time.sleep(1)
    return triple_checker(user_input_list)

def restart_check():
    user_input = input("\nWould you like to try again? (y/n):\n")
    if user_input == 'y':
        print(input_handler())
        restart_check()
    elif user_input == 'n':
        print("Goodbye.")
        return
    else:
        print("I don't understand.")
        time.sleep(1)
        restart_check()


print("Welcome to Pythagorean Triples Checker!\n")
print(input_handler())
restart_check()
