import numpy as np

# --------------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------------
# creates board
def create_board():
    board = [[0 for y in range(8)] for x in range(8)]
    return board

# prints board in 8x8 array
def print_board(board):
    for x in range(8):
        print(board[x])

# calculates movements needed for piece to make move
def calc_move(piece, move):
    move = []
    for x in range(2):
        move.append(piece.currentPosition[x] - move[x])
    return(move)


# -----------------------------------------------------------
# RUN GAME
# -----------------------------------------------------------
is_running = False

while is_running == True:
     print("wip")

# ---------------------------------------------------------
# CLASSES
# ---------------------------------------------------------
class Rook:
    # initialize a rook
    def __init__(self, currentPosition):
        self.currentPosition = currentPosition

    # check if move is possible using calc_move
    def checkMove(move):
        check = calc_move(self, move)
        print(check)

# class Pawn:
    # initialize a pawn
#     def __init__(self, currentPosition):
#         self.currentPosition = currentPosition
#
    # check if move is possible using calc_move
#     def checkMove(self):
#         pass


# -----------------------------------------------------------
# TESTING / WIP
# -----------------------------------------------------------

wrook1 = Rook([0, 0])
print (wrook1.currentPosition)

for x in range(2):
    list_diff.append(list1[x] - list2[x])

print(list_diff)
