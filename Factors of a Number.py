## def a function that creates a list of factors from user input
# should be in ascending order
# 1 should be included

def factor(user_input):
    return [x for x in range(1, user_input + 1) if user_input % x == 0]

if __name__ == "__main__":
    while True:
        try:
            user_input = int(input("\nWhat is your number? "))
            print(factor(user_input))
            break
        except:
            print("Sorry, that is not a valid number")
    