
# Drawing the board:
sign_rows = 12
sign_columns = 15
playable_rows = int(sign_rows/2)
playable_columns = int((sign_columns-1)/2)

#                                                   #   COLUMNS --->
currentField = [[" ", " ", " ", " ", " ", " "],     # R
                [" ", " ", " ", " ", " ", " "],     # O
                [" ", " ", " ", " ", " ", " "],     # W
                [" ", " ", " ", " ", " ", " "],     # S
                [" ", " ", " ", " ", " ", " "],     # |
                [" ", " ", " ", " ", " ", " "],     # |
                [" ", " ", " ", " ", " ", " "]]     # V


def draw_board(sign_rows, sign_columns):
    for row in range(sign_rows):                                #
        if row % 2 == 0:                                        #
            for col in range(sign_columns):                     #
                if col % 2 == 0 and col == sign_columns - 1:    #
                    print("|")                                  #
                elif col % 2 == 0:
                    print("|", end="")
                else:
                    Col = int((col-1)/2)
                    Row = int(row/2)
                    print(currentField[Col][Row], end="")
        else:
            print("-" * sign_columns)


draw_board(sign_rows, sign_columns)

#Checking for winner:
def check_for_win():

#Checking for horizontal lines:
    for y in range(playable_rows):
        for x in range(playable_columns - 3):
            if currentField[x][y] != " " and currentField[x][y] == currentField[x+1][y] and currentField[x][y] == currentField[x+2][y] and currentField[x][y] == currentField[x+3][y]:
                End1 = 1
                Winner = currentField[x][y]
                print("Player "+ Winner + " has won! You 'connected 4' in row " + str(6-y) + "\n" )

            else:
                End1 = 0


#Checking for vertical lines:
    for x in range(playable_columns):
        for y in range(playable_rows - 3):
            if currentField[x][y] != " " and currentField[x][y] == currentField[x][y+1] and currentField[x][y] == currentField[x][y+2] and currentField[x][y] == currentField[x][y+3]:
                End2 = 1
                Winner = currentField[x][y]
                print("Player " + Winner + " has won! You 'connected 4' in column " + str(x+1) + "\n")
            else:
                End2 = 0


#Checking for diagonals:
    for x in range(playable_columns - 3):
        for y in range(playable_rows - 3):
            if currentField[x][y] != " " and currentField[x][y] == currentField[x+1][y+1] and currentField[x][y] == currentField[x+2][y+2] and currentField[x][y] == currentField[x+3][y+3]:
                End3 = 1
                Winner = currentField[x][y]
                print("Player " + Winner + " has won! You 'connected 4' in a Diagonal from top left to down right starting in column " + str(x+1) + "and on line " + str(y+1) + "\n")
            else:
                End3 = 0


    for x in range(playable_columns - 3,-1,-1):
        for y in range(playable_rows - 3,-1,-1):
            if currentField[x][y] != " " and currentField[x][y] == currentField[x-1][y-1] and currentField[x][y] == currentField[x-2][y-2] and currentField[x][y] == currentField[x-3][y-3]:
                End4 = 1
                Winner = currentField[x][y]
                print(
                    "Player " + Winner + " has won! You 'connected 4' in a Diagonal from top right to down left starting in column " + str(x+1) + "and on line " + str(y+1) + "\n")
            else:
                End4 = 0

    if End1 == 1 or End2 == 1 or End3 == 1 or End4 == 1:
        End = 1

    else:
        End = 0

    return End



# Playing algorithm
Player = 1

rowcount = [-1, -1, -1, -1, -1, -1, -1]

while check_for_win() == 0:
    if Player == 1:
        chosen_column1 = (int(input("Player 1: Which column do want to put your Stone in?\n"))-1)
        if 0 <= chosen_column1 <= 6:
            currentField[chosen_column1][rowcount[chosen_column1]] = "O"
            rowcount[chosen_column1] -= 1
            Player = 2
            draw_board(sign_rows, sign_columns)
            check_for_win()
        else:
            print("Enter a Number between 1 and 7!")
            Player = 1

    else:
        chosen_column2 = (int(input("Player 2: Which column do want to put your Stone in?\n"))-1)

        if 0 <= chosen_column2 <= 6:
            currentField[chosen_column2][rowcount[chosen_column2]] = "X"
            rowcount[chosen_column2] -= 1
            Player = 1
            draw_board(sign_rows, sign_columns)
            check_for_win()

        else:
            print("Enter a Number between 1 and 7!")
            Player = 2

print("End of Game")
