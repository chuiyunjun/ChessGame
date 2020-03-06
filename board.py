import pygame

from king import King
from queen import Queen
from rook import Rook
from bishop import Bishop
from knight import Knight
from pawn import Pawn

class Board():
    def __init__(self, window):
        self.window = window
        window.fill(pygame.Color(179, 199, 199))
        # window.fill(pygame.Color(0, 0, 0))
        self.board = [[None for y in range(8)] for x in range(8)]

        self.pieces_image = []
        for color in ["black_", "white_"]:
            for piece in ["king", "queen", "bishop", "knight", "rook", "pawn"]:
                image = pygame.image.load(color + piece + ".png")
                image = pygame.transform.scale(image, (80, 80))
                self.pieces_image.append(image)

        self.initializePieces()

    def initializePieces(self):
        self.board[4][0] = King(self.window, False, 4, 0, self.pieces_image[0])
        self.board[3][0] = Queen(self.window, False, 3, 0, self.pieces_image[1])
        self.board[0][0] = Rook(self.window, False, 0, 0, self.pieces_image[4])
        self.board[7][0] = Rook(self.window, False, 7, 0, self.pieces_image[4])
        self.board[6][0] = Knight(self.window, False, 6, 0, self.pieces_image[3])
        self.board[1][0] = Knight(self.window, False, 1, 0, self.pieces_image[3])
        self.board[2][0] = Bishop(self.window, False, 2, 0, self.pieces_image[2])
        self.board[5][0] = Bishop(self.window, False, 5, 0, self.pieces_image[2])

        self.board[4][7] = King(self.window, True, 4, 7, self.pieces_image[0 + 6])
        self.board[3][7] = Queen(self.window, True, 3, 7, self.pieces_image[1 + 6])
        self.board[0][7] = Rook(self.window, True, 0, 7, self.pieces_image[4 + 6])
        self.board[7][7] = Rook(self.window, True, 7, 7, self.pieces_image[4 + 6])
        self.board[6][7] = Knight(self.window, True, 6, 7, self.pieces_image[3 + 6])
        self.board[1][7] = Knight(self.window, True, 1, 7, self.pieces_image[3 + 6])
        self.board[2][7] = Bishop(self.window, True, 2, 7, self.pieces_image[2 + 6])
        self.board[5][7] = Bishop(self.window, True, 5, 7, self.pieces_image[2 + 6])

        white = False
        for y in [1, 6]:
            for x in range(8):
                if y == 6:
                    white = True

                if white:
                    image = self.pieces_image[5 + 6]
                else:
                    image = self.pieces_image[5]

                self.board[x][y] = Pawn(self.window, white, x, y, image)

    def draw_board(self):
        white = True
        for x in range(8):
            for y in range(8):
                xpos = 30 + x * 80
                ypos = 30 + y * 80
                rect = pygame.Rect(xpos, ypos, 80, 80)
                if white:
                    color = pygame.Color(217, 217, 217)
                else:
                    color = pygame.Color(66, 66, 66)

                pygame.draw.rect(self.window, color, rect)
                
                if self.board[x][y] is not None:
                    self.board[x][y].draw()

                if (y != 7):
                    white = not white

        pygame.display.flip()

        # optimize to piece by piece drawing using pygame.update

    def get_item(self, xPos, yPos):
        if 0 <= xPos <= 7 and 0 <= yPos <= 7:
            return self.board[xPos][yPos]
        return None

    def get_board(self):
        return self.board