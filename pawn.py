from piece import Piece

import pygame

class Pawn(Piece):
    def __init__(self, window, white, xPos, yPos, sprite):
        super().__init__(window, white, xPos, yPos, sprite)
        self.doubleMoveLast = False;


    def move_piece(self, xPos, yPos, board):
        originalYPos = self.yPos
        successfulMove = super().move_piece(xPos, yPos, board)
        if successfulMove is not None and self.doubleMoveLast:
            self.doubleMoveLast = False

        if successfulMove is not None and abs(yPos - originalYPos) == 2:
            self.doubleMoveLast = True
        return successfulMove

    def Possible_moves(self, board):
        moves = []
        change = 1
        if self.white:
            change = -1

        # single move
        if board[self.xPos][self.yPos + change] is None:
            moves.append((self.xPos, self.yPos + change, "N"))

        # double move
        if not self.moved:
            moves.append((self.xPos, self.yPos + change * 2, "N"))

        # capture move
        for inc in [1, -1]:
            if not (0 <= self.xPos + inc <= 7):
                continue

            if board[self.xPos + inc][self.yPos + change] is not None and \
                board[self.xPos + inc][self.yPos + change].white != self.white:
                moves.append((self.xPos + inc, self.yPos + change, "N"))

            if isinstance(board[self.xPos + inc][self.yPos], Pawn) and \
                board[self.xPos + inc][self.yPos].white != self.white and \
                board[self.xPos + inc][self.yPos].doubleMoveLast:
                moves.append((self.xPos + inc, self.yPos + change, "E"))

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