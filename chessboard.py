import numpy as np

def create_board():
    board = [[0 for y in range(8)] for x in range(8)]
    return board

def print_board(board):
    for x in range(8):
        print(board[x])

board = create_board()
print_board(board)

is_running = False

while is_running == True:
     print("wip")

#Create classes for each piece (pawn, rook, bishop, knight, king) and then have two child classes for each piece to seperate them between white and black?
#No need for queen class since you can simply combine rook and bishop (?), can you have a child class that inherits from two different classes?

class Rook:
    def __init__(self, currentPosition):
        self.currentPosition = currentPosition
    def checkMove(self):
        pass
        #Need to take the initial position in form [x][y] then check to see if move is in either [x][0-8] or [0-8][y], if so, return true, if not, return false -> don't worry about pieces blocking way for now??

class Pawn:
    def __init__(self, currentPosition):
        self.currentPosition = currentPosition
    def checkMove(self):
        pass
