from replit import clear


#draw board
def draw_board(board):
    print("  1|2|3")
    print(f"1 {board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("_______")
    print(f"2 {board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("_______")
    print(f"3 {board[2][0]}|{board[2][1]}|{board[2][2]}")
    print()

#short info
def introduction():
    print("Player in turn gives first the column between 1 and 1 and row between 1 and 3")
    print("For example 11 marks top lef corner of the board")
    print("Aim is to get three in line either horizontal, vertical or crossing the board")


def check_board(x_cor, y_cor, board):
    if board[x_cor - 1][y_cor - 1] == " ":
        return True
    else:
        return False


def check_winner(board, player):
    #check row 1
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    #check row 2
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    #check row 3
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    #check column 1
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    #check column 2
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    #check column 3
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    #check crossing 1
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    #check crossing 2
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False


def game():
    #set up the board and display info and empty board
    board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    introduction()
    draw_board(board)

    #player 1 can choose mark
    player_1 = input("Choose your mark ( X or O, other=introduction): ").upper()
    player_2 = ("X" if player_1 == "O" else "O").upper()
    print(f"Player 1 is {player_1} and player 2 is {player_2}")

    turn = 1
    player = ""

    game_on = True

    while game_on:
        # if turn over 9, board is full and no winner
        if turn > 9:
            game_on = False
            print("GAME OVER! Tie game")
            break

        #determine which players turn it is
        if turn % 2 != 0:
            player = player_1
        else:
            player = player_2

        row = int(input(f"Player {player}, choose your row between 1 and 3: "))
        column = int(input(f"Player {player}, choose your column between 1 and 3: "))

        if 0 <= row - 1 <= 2 and 0 <= column - 1 <= 2:
            if check_board(row, column, board):
                board[row - 1][column - 1] = player
                draw_board(board)
                if check_winner(board, player):
                    game_on = False
                    print(f"GAME OVER! Player {player} wins!")
                turn += 1
            else:
                print("Already filled. Choose another")
        else:
            print("Out of bound. Choose another")


def main():
    input1 = input("Want to play a game of tic-tac-toe? (yes/no): ")
    play_game = 1 if input1 == "yes" else 0

    while play_game == 1:
        game()

        input2 = input("Want to a play another game? (yes/no): ")
        if input2 == "yes":
            clear()
            game()
        else:
            break

main()




