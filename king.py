from piece import Piece
from rook import Rook
import pygame

class King(Piece):
    def __init__(self, window, white, xpos, ypos, sprite):
        super().__init__(window, white, xpos, ypos, sprite)
        self.moved = False

    def possible_moves(self, board):
        moves = [(x + self.xpos, y + self.ypos) for x in [1, 0 -1] for y in [1, 0 -1]]
        moves.remove((self.xpos, self.ypos))

        # check castling
        if self.moved:
            pass
        elif self.white:
            rook1 = board[0][7]
            rook2 = board[7][7]
            # add castling
            if isinstance(rook1, Rook) and not rook1.moved and rook1.white:
                pass
            if isinstance(rook2, Rook) and not rook2.moved and rook2.white:
                pass
        else:
            rook1 = board[0][0]
            rook2 = board[7][0]
            # add castling
            if isinstance(rook1, Rook) and not rook1.moved and not rook1.white:
                pass
            if isinstance(rook2, Rook) and not rook1.moved and not rook1.white:
                pass

        removals = []
        for move in moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                removals.append(move) 

        for removal in removals:
            moves.remove(removal)
            
        return moves

    def draw(self):
        # if self.drawn:
        #   return False

        self.window.blit(self.sprite, (self.xpos * 80 + 30, self.ypos * 80 + 30))
        self.drawn = False
        return True