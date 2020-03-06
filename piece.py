class Piece():
    # xpos ypos shold be given as the pieces index on
    # the 2d array of board
    def __init__(self, window, white, xpos, ypos, sprite):
        self.window = window
        self.white = white
        self.xpos = xpos
        self.ypos = ypos
        self.drawn = False
        self.sprite = sprite

    def draw(self):
        raise NotImplementedError

    def move_piece(self, xpos, ypos, board):
        if (xpos, ypos) in self.possible_moves(board):
            self.xpos = xpos
            self.ypos = ypos
            return True
        return False

    def possible_moves(self, board):
        raise NotImplementedError

