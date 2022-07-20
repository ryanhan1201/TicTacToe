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
    #def check_win():
    def check_loc(i, j):
        return board[i][j] != ' '
    turn_counter = 0
    while not is_filled():
        #if turn counter is even then its P1's turn
        #if turn counter is odd then its P2's turn
        loc = 0
        print("Where do you wish to place your marker?")
        if turn_counter % 2 == 0:
            loc = int(input())
            x = int(loc / 3)
            y = loc % 3
            if check_loc(x, y):
                print("That location is filled. Try again")
                turn_counter -= 1
            else:
                board[x][y] = 'O'
        else:
            loc = int(input())
            x = int(loc / 3)
            y = loc % 3
            if check_loc(x, y):
                print("That location is filled. Try again")
                turn_counter -= 1
            else:
                board[x][y] = 'X'
        turn_counter += 1
        print_board(board)


main()
#TODO: Implement win checker, also error check if input of location is too high 