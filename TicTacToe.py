
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def displayBoard():
    for i in board:
        print("-------------")
        print("|", i[0], "|", i[1], "|", i[2], "|")
    print("-------------")

def checkWinner(player):
    # Rows
    for i in board:
        if i[0] == player and i[1] == player and i[2] == player:
            return True
        
    # Columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        
    # Diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

user = "X"
moves = 0
won = False

print("Assume that columns are numbered top to bottom, and rows are numbered left to right (Top left would be 1,1).")

while moves < 9:
    displayBoard()
    print("\n")
    print(f"{user}'s turn")
    print("\n")
    row = int(input("Input row number ... ")) - 1
    column = int(input("Input column number ...")) - 1

    if board[row][column] == " ":
        board[row][column] = user
        moves += 1

        if checkWinner(user) == True:
            won = True
            print("\n")
            displayBoard()
            print("\n")
            print(f"{user} wins!")
            break
        
        if user == "X":
            user = "O"
        elif user == "O":
            user = "X"

    else:
        print("Space already taken... ")

if won == False:
    print("\n")
    displayBoard()
    print("\nDraw!")    


