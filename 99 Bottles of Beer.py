def bottles():
    number_of_bottles = 99
    while number_of_bottles > 1:
        print("{b} bottles of beer on the wall, {b} bottles of beer.\nTake one down and pass it around, {b2} bottles of beer on the wall.\n".format(b=number_of_bottles, b2=number_of_bottles-1))
        number_of_bottles -= 1
    else:
        print("{b} bottle of beer on the wall, {b} bottle of beer.\nTake one down and pass it around, {b2} bottles of beer on the wall.".format(b=number_of_bottles, b2=number_of_bottles-1))

bottles()