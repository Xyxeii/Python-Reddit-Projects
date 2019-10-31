##find the number fitting the following criteria
#The number has two or more digits
#The number is prime
#The number does NOT contain a 1 or 7 in it
#The sum of all digits is less than or equal to 10
#The first two digits add up to be odd
#The second to last digit is even
#The last digit is equal to how many digits are in the number

import timeit

def what_is_my_number(start_point, end_point, without_zero = True):
    possible_numbers = []
    #address containing a 1 and two or more digits
    if start_point < 20:
        start_point += 20 - start_point
    for number in range(start_point, end_point):
        str_number = str(number)
    #prime number check; will always be > 1 due to startpoint check
        if not "1" in str_number or "7" in str_number:
            if isPrime(number):
                odd_checker = (int(str_number[0]) + int(str_number[1])) % 2 != 0
                if without_zero:
                    even_checker = False if int(str_number[-2]) == 0 else int(str_number[-2]) % 2 == 0
                else:
                    even_checker = int(str_number[-2]) % 2 == 0
                last_digit_checker = int(str_number[-1])
                if odd_checker == True and even_checker == True and last_digit_checker == len(str_number):
                    possible_numbers.append(str_number)
    print(f"Possible Numbers after initial check: {possible_numbers}")
    for number in possible_numbers:
        number_sum = 0
        for digit in number:
            number_sum += int(digit)
        if number_sum <= 10:
            return f"Magic Number is {number}"

def isPrime(Number):
    return 2 in [Number,2**Number%Number]

if __name__ == "__main__":
    start = timeit.default_timer()
    ##3rd arg True to count zero as odd to get projects' intended results. Otherwise ouput is 503 which also meets the project requirements
    print(what_is_my_number(1, 1000, True))
    stop = timeit.default_timer()
    print(f"Runtime: {stop - start}")