def fib():
    while True:
        try:
            user_input = int(input("TYPE A NUMBER: "))
            break
        except:
            print("Type a number idiot")
    fib_sequence = [0, 1]
    if user_input > 1:
        for x in range(user_input - 1):
            fib_sequence.append(fib_sequence[x] + fib_sequence[x+1])
    else:
        return fib_sequence[user_input]
    return fib_sequence[user_input-1] + fib_sequence[user_input - 2]

print(fib())
