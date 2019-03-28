def board_printer(row,column):
    for i in range(0,row):
        print(" ---" * column)
        print("|   " *(column+1))

    print(" ---" * column)

row = int(input("Please enter the number of rows needed: "))
column = int(input("Please enter the number of columns needed: "))

board_printer(row,column)