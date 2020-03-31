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
def calc_move(currentPosition, dest):
    move = []
    for x in range(2):
        move.append(currentPosition[x] - dest[x])
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
    def checkMove(self, move):
        currentPosition = self.currentPosition
        check = calc_move(currentPosition, move)
        print("--------------------------------------------")
        print("currentpos: " + str(self.currentPosition))
        print("move dest: " + str(move))

        # if rook is moving along the y-axis
        if check[0] == 0:
            # if move dest is the same as currentPosition
            if check[1] == 0:
                print("invalid move: can't move in place")
            # check for out-of-bounds move
            else:
                if (move[1] > 8 or move[1] < 0):
                    print("invalid move: move out of bounds")
                # valid move
                else:
                    self.currentPosition[1] = move[1]
                    print("new position: " + str(self.currentPosition))
        # if rook is moving along the x-axis
        if check[1] == 0:

            # check for out-of-bounds move
                if (move[0] > 8 or move[0] < 0):
                    print("invalid move: move out of bounds")

                else:
                    self.currentPosition[0] = move[0]
                    print("new position: " + str(self.currentPosition))

        if(check[0]!= 0 and check[1]!= 0):
            print("invalid move: can only move along one axis at a time")

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

rook = Rook([0,0])
rook.checkMove([3,0])
rook.checkMove([0,0])
rook.checkMove([0,3])
rook.checkMove([0,0])
rook.checkMove([1,1])
rook.checkMove([0,9])
rook.checkMove([0,-1])
rook.checkMove([9,0])
rook.checkMove([-1,0])
