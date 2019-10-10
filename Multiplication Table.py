##ReadMe
#multiplication table the size of a user inputted value. Cap this?
#acount for character length when spacing. Apply the space before the character

def multiplication_table():
    while True:
        try:
            table_length = int(input("What is the length of the table? "))
            break
        except:
            print("I'm sorry that is not a valid number value.")
    table_column = ["X"] + [x for x in range(table_length + 1)]
    max_length = max(table_column[1:])
    for row in table_column:
        table_row = []
        for cell in range(len(table_column)):
            if row == "X":
                if cell >= 1:
                    if len(str(cell - 1)) < len(str(max_length * max_length)):
                        table_row.append(" " * (len(str(max_length * max_length)) - len(str(cell - 1))))
                    table_row.append(" " + str(cell - 1))
                else:
                    table_row.append(" " * (len(str(max_length * max_length)) - len(str(cell - 1))) + str(row))
            else:
                spacing = " " * (len(str(max_length * max_length)) - len(str((cell - 1) * row)))
                if cell >= 1:
                    if len(str((cell - 1)*row)) < len(str(max_length * max_length)):
                        table_row.append(spacing)
                    table_row.append(" " + str((cell - 1) * row))
                else:
                    table_row.append(spacing + str(row))
        print("".join(table_row))



multiplication_table()
