from piece import Piece

import pygame

class Rook(Piece):
    def __init__(self, window, white, xpos, ypos, sprite):
        super().__init__(window, white, xpos, ypos, sprite)
        self.moved = False

    def possible_moves(self, board):
        moves = []
        for increment in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            currX = self.xpos + increment[0]
            currY = self.ypos + increment[1]
            while 0 <= currX <= 7 and 0 <= currY <= 7:
                if board[currX][currY] is None:
                    moves.append((currX, currY))

                elif board[currX][currY].white is not self.white:
                    moves.append((currX, currY))
                    break

                else:
                    break

                currX += increment[0]
                currY += increment[1]
                print(currX, currY)

        return moves

    def draw(self):
        # if self.drawn:
        #   return False

        self.window.blit(self.sprite, (self.xpos * 80 + 30, self.ypos * 80 + 30))
        self.drawn = False
        return True