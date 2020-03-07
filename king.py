from piece import Piece

from rook import Rook

import pygame

class King(Piece):
    def __init__(self, window, white, xPos, yPos, sprite):
        super().__init__(window, white, xPos, yPos, sprite)

    def Possible_moves(self, board):
        moves = [(x + self.xPos, y + self.yPos, "N") for x in [1, 0, -1] for y in [1, 0, -1]]
        moves.remove((self.xPos, self.yPos, "N"))

        # check castling
        if self.white:
            rook1 = board[0][7]
            rook2 = board[7][7]
        else:
            rook1 = board[0][0]
            rook2 = board[7][0]

        # check for contested and check and blocks in the way
        if isinstance(rook1, Rook) and not rook1.moved and not self.moved and \
            all(board[i][self.yPos] is None for i in range(1, 4)):
            moves.append((2, self.yPos, "C"))

        if isinstance(rook2, Rook) and not rook2.moved and not self.moved and \
            all(board[i][self.yPos] is None for i in range(5, 7)):
            moves.append((6, self.yPos, "C"))

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

        self.window.blit(self.sprite, (self.xPos * 80 + 30, self.yPos * 80 + 30))
        self.drawn = False
        return True