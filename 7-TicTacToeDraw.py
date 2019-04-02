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
            print(game[0])
            print(game[1])
            print(game[2])

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
            print(game[0])
            print(game[1])
            print(game[2])


        else:
            print("Error! the coordinates you have chosen is invalid")

    if counter == 9:
        print("The game has ended!")
        break