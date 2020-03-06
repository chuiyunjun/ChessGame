from piece import Piece

import pygame

class Pawn(Piece):
    def __init__(self, window, white, xpos, ypos, sprite):
        super().__init__(window, white, xpos, ypos, sprite)
        self.moved = False


    def possible_moves(self, board):
        moves = []
        if self.white:
            # single move
            if board[self.xpos][self.ypos - 1] is None:
                moves.append((self.xpos, self.ypos - 1))

            # double move
            if not self.moved:
                moves.append((self.xpos, self.ypos - 2))

            # capture move
            for inc in [1, -1]:
                if not (0 <= self.xpos + inc <= 7):
                    pass
                elif board[self.xpos + inc][self.ypos - 1] is not None and \
                    board[self.xpos + inc][self.ypos - 1].white != self.white:
                    moves.append((self.xpos + inc, self.ypos - 1))

            print(moves)

        else:
            # single move
            if board[self.xpos][self.ypos + 1] is None:
                moves.append((self.xpos, self.ypos + 1))

            # double move
            if not self.moved:
                moves.append((self.xpos, self.ypos + 2))

            # capture move
            for inc in [1, -1]:
                if not (0 <= self.xpos + inc <= 7):
                    pass
                elif board[self.xpos + inc][self.ypos + 1] is not None and \
                    board[self.xpos + inc][self.ypos + 1].white != self.white:
                    moves.append((self.xpos + inc, self.ypos + 1))

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