import numpy as np

def print_board(board):
    print(board[0][0] , "|" , board[0][1] , "|" , board[0][2])
    print("-- --- --")
    print(board[1][0] , "|" , board[1][1] , "|" , board[1][2])
    print("-- --- --")
    print(board[2][0] , "|" , board[2][1] , "|" , board[2][2])

def main():
    board = np.array([[' ']*3, [' ']*3, [' ']*3])
    #get user input from 0-9 which reps a cell in grid
    #0 is top left and 9 bottom right
    def is_filled():
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return False
        return True
    def check_win(turn):
        #there are 8 three in a rows so make vars for each win con
        con1 = board[0][0] == board[0][1] and board[0][0] == board[0][2]
        con2 = board[1][0] == board[1][1] and board[1][0] == board[1][2]
        con3 = board[2][0] == board[2][1] and board[2][0] == board[2][2]
        con4 = board[0][0] == board[1][0] and board[0][0] == board[2][0]
        con5 = board[0][1] == board[1][1] and board[0][1] == board[2][1]
        con6 = board[0][2] == board[1][2] and board[0][2] == board[2][2]
        con7 = board[0][0] == board[1][1] and board[0][0] == board[2][2]
        con8 = board[0][2] == board[1][1] and board[0][2] == board[2][0]

        if turn % 2 == 0:
            #checking for O win
            return (con1 and board[0][0] == 'O') or (con2 and board[1][0] == 'O') or (con3 and board[2][0] == 'O') or (con4 and board[0][0] == 'O') or (con5 and board[0][1] == 'O') or (con6 and board[0][2] == 'O') or (con7 and board[0][0] == 'O') or (con8 and board[0][2] == 'O')
        else:
            #checking for X win
            return (con1 and board[0][0] == 'X') or (con2 and board[1][0] == 'X') or (con3 and board[2][0] == 'X') or (con4 and board[0][0] == 'X') or (con5 and board[0][1] == 'X') or (con6 and board[0][2] == 'X') or (con7 and board[0][0] == 'X') or (con8 and board[0][2] == 'X')

    def check_loc(i, j):
        return board[i][j] != ' '
    print_board(board)
    turn_counter = 0
    win_con = False
    while not is_filled() and not win_con:
        #if turn counter is even then its P1's turn
        #if turn counter is odd then its P2's turn
        loc = 0
        print("Where do you wish to place your marker?")
        if turn_counter % 2 == 0:
            loc = int(input())
            x = int(loc / 3)
            y = loc % 3
            if loc > 9:
                print("That is not a playable space.")
                print("Try Again")
                turn_counter -= 1
            elif check_loc(x, y):
                print("That location is filled.")
                print("Try again")
                turn_counter -= 1
            else:
                board[x][y] = 'O'
        else:
            loc = int(input())
            x = int(loc / 3)
            y = loc % 3
            if loc >= 9:
                print("That is not a playable space.")
                print("Try Again")
                turn_counter -= 1
            elif check_loc(x, y):
                print("That location is filled. Try again")
                turn_counter -= 1
            else:
                board[x][y] = 'X'
        print_board(board)
        win_con = check_win(turn_counter)
        turn_counter += 1
    if win_con:
        winner = 0
        if turn_counter % 2 == 0:
            winner = 2
        else:
            winner = 1
        print("The Winner Is Player", winner)
    else:
        print("Its A TIE")

main()