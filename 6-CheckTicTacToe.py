def TTT_checker(grid):

    for x in range(0,3):
        row = set([grid[x][0],grid[x][1],grid[x][2]])
        if len(row) == 1 and grid[x][0] != 0:
            return print("The winner is player {}" .format(grid[x][0]))


    for x in range(0,3):
        column = set([grid[0][x],grid[1][x],grid[2][x]])
        if len(column) == 1 and grid[0][x] != 0:
            return print("The winner is player {}" .format(grid[0][x]))


    diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
    diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        return print("The winner is player {}".format(grid[1][1]))

    return print("Its a tie!")



board = [[1,2,0],
         [2,1,0],
         [2,1,1] ]

winner_is_2 = [[2,2,0],
         [2,1,0],
         [2,1,1] ]

winner_is_1 = [[1,2,0],
         [2,1,0],
         [2,1,1] ]

winner_is_also_1 = [[0,1,0],
         [2,1,0],
         [2,1,1] ]

no_winner = [[1,2,0],
         [2,1,0],
         [2,1,2] ]

also_no_winner = [[1,2,0],
         [2,1,0],
         [2,1,0] ]

TTT_checker(board)
TTT_checker(winner_is_2)
TTT_checker(winner_is_1)
TTT_checker(winner_is_also_1)
TTT_checker(no_winner)
TTT_checker(also_no_winner)

