# Single-player game of Battleship with one ship and 4 turns

from random import randint

board = []

for x in range(5): # creates 5x5 board
    board.append(["O"] * 5)

def print_board(board): # prints board for user
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board): # chooses random row
    return randint(0, len(board) - 1)

def random_col(board): # chooses random column
    return randint(0, len(board[0]) - 1)

# sets coordinates of hidden battleship at random
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print "Turn {0}".format(turn+1)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Column:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break  
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            
        if turn == 3:
            print "Game Over"
    # Print (turn + 1) here!
    print turn + 1
    print_board(board)
