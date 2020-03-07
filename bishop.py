from piece import Piece

import pygame

class Bishop(Piece):
    def __init__(self, window, white, xPos, yPos, sprite):
        super().__init__(window, white, xPos, yPos, sprite)


    def Possible_moves(self, board):
        moves = []
        for increment in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            currX = self.xPos + increment[0]
            currY = self.yPos + increment[1]
            while 0 <= currX <= 7 and 0 <= currY <= 7:
                if board[currX][currY] is None:
                    moves.append((currX, currY, "N"))

                elif board[currX][currY].white is not self.white:
                    moves.append((currX, currY, "N"))
                    break

                else:
                    break

                currX += increment[0]
                currY += increment[1]

        return moves

    def draw(self):
        # if self.drawn:
        #   return False

        self.window.blit(self.sprite, (self.xPos * 80 + 30, self.yPos * 80 + 30))
        self.drawn = False
        return True