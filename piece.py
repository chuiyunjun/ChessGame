class Piece():
    # xpos ypos shold be given as the pieces index on
    # the 2d array of board
    def __init__(self, window, white, xPos, yPos, sprite):
        self.window = window
        self.white = white
        self.xPos = xPos
        self.yPos = yPos
        self.drawn = False
        self.sprite = sprite
        self.moved = False

    def draw(self):
        raise NotImplementedError

    def move_piece(self, xPos, yPos, board):
        for move in self.Possible_moves(board):
            if (xPos, yPos) == (move[0], move[1]):
                return move
        return None

    def Possible_moves(self, board):
        raise NotImplementedError

