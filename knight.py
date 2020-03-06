from piece import Piece

import pygame

class Knight(Piece):
    def __init__(self, window, white, xpos, ypos, sprite):
        super().__init__(window, white, xpos, ypos, sprite)


    def possible_moves(self, board):
        moves = []
        moves.extend([(x + self.xpos, y + self.ypos) for x in [2, -2] for y in [1, -1]])
        moves.extend([(x + self.xpos, y + self.ypos) for y in [2, -2] for x in [1, -1]])
        removals = []
        for move in moves:
            if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
                removals.append(move) 
                continue

            piece = board[move[0]][move[1]]
            if piece is not None and piece.white == self.white:
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