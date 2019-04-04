def board_printer(grid):
    row = 3
    column = 3


    for i in range(0,row):
        if i != 0:
            print("")
        print(" ---" * column)
        for j in range(0,column):
            print("| {} " .format(grid[i][j]), end = "")

    print("")
    print(" ---" * column)


def TTT_checker(grid):

    for x in range(0,3):
        row = set([grid[x][0],grid[x][1],grid[x][2]])
        if len(row) == 1 and grid[x][0] != 0:
            return grid[x][0]


    for x in range(0,3):
        column = set([grid[0][x],grid[1][x],grid[2][x]])
        if len(column) == 1 and grid[0][x] != 0:
            return grid[0][x]


    diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
    diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return grid[1][1]


game = [["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]
player = True
counter = 0

while True:
    if player:
        player_1_input = (input("Player 1 - Please enter coordinates (e.g. 1,2): ")).split(",")
        row_1 = int(player_1_input[0])-1
        column_1 = int(player_1_input[1])-1

        if game[row_1][column_1] != "X" and game[row_1][column_1] != "O":
            game[row_1][column_1] = "X"
            counter = counter + 1
            player = False
            board_printer(game)

            if TTT_checker(game) == "X":
                print("The winner is player 1")
                break
            elif TTT_checker(game)=="O":
                print("The winner is player 2")


        else:
            print("Error! the coordinates you have chosen is invalid")

    else:
        player_2_input = (input("Player 2 - Please enter coordinates (e.g. 1,2): ")).split(",")
        row_2 = int(player_2_input[0]) - 1
        column_2 = int(player_2_input[1]) - 1

        if game[row_2][column_2] != "X" and game[row_2][column_2] != "O":
            game[row_2][column_2] = "O"
            counter = counter + 1
            player = True
            board_printer(game)

            if TTT_checker(game) == "X":
                print("The winner is player 1")
                break
            elif TTT_checker(game) == "O":
                print("The winner is player 2")

        else:
            print("Error! the coordinates you have chosen is invalid")

    if counter == 9:
        if TTT_checker(game) == "X":
            print("The winner is player 1")
            break
        elif TTT_checker(game) == "O":
            print("The winner is player 2")
        else:
            print("Its a Tie")
        break