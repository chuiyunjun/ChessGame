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

        self.turn = True # True is white False is black

        self.selected = None

        self.pieces_image = []
        for color in ["black_", "white_"]:
            for piece in ["king", "queen", "bishop", "knight", "rook", "pawn"]:
                image = pygame.image.load(color + piece + ".png")
                image = pygame.transform.scale(image, (80, 80))
                self.pieces_image.append(image)

        self.black_pawns = []
        self.white_pawns = []
        self.black_king = None
        self.white_king = None

        self.initializePieces()


    def initializePieces(self):
        self.board[4][0] = King(self.window, False, 4, 0, self.pieces_image[0])
        self.black_king = self.board[4][0]

        self.board[3][0] = Queen(self.window, False, 3, 0, self.pieces_image[1])
        self.board[0][0] = Rook(self.window, False, 0, 0, self.pieces_image[4])
        self.board[7][0] = Rook(self.window, False, 7, 0, self.pieces_image[4])
        self.board[6][0] = Knight(self.window, False, 6, 0, self.pieces_image[3])
        self.board[1][0] = Knight(self.window, False, 1, 0, self.pieces_image[3])
        self.board[2][0] = Bishop(self.window, False, 2, 0, self.pieces_image[2])
        self.board[5][0] = Bishop(self.window, False, 5, 0, self.pieces_image[2])

        self.board[4][7] = King(self.window, True, 4, 7, self.pieces_image[0 + 6])
        self.white_king = self.board[4][7]

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

                if white:
                    self.white_pawns.append(self.board[x][y])
                else:
                    self.black_pawns.append(self.board[x][y])

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

    def contested(self, white, xPos, yPos):
        # checks for knights
        moves = []
        moves.extend([(x + xPos, y + yPos, "N") for x in [2, -2] for y in [1, -1]])
        moves.extend([(x + xPos, y + yPos, "N") for y in [2, -2] for x in [1, -1]])
        for move in moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and \
                isinstance(self.board[move[0]][move[1]], Knight) and \
                self.board[move[0]][move[1]].white != white:
                return True
        print("past knight")
        # checks for rooks / queens
        for increment in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            currX = xPos + increment[0]
            currY = yPos + increment[1]
            while 0 <= currX <= 7 and 0 <= currY <= 7:
                if (self.board[currX][currY] is not None) and \
                    not isinstance(self.board[currX][currY], Queen) and \
                    not isinstance(self.board[currX][currY], Rook):
                    break

                if (isinstance(self.board[currX][currY], Queen) or \
                    isinstance(self.board[currX][currY], Rook)) and \
                    self.board[currX][currY].white != white:
                    return True

                currX += increment[0]
                currY += increment[1]
        print("past rooks/queens")
        # checks for bishops / queens
        for increment in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            currX = xPos + increment[0]
            currY = yPos + increment[1]
            while 0 <= currX <= 7 and 0 <= currY <= 7:
                if (self.board[currX][currY] is not None) and \
                    not isinstance(self.board[currX][currY], Queen) and \
                    not isinstance(self.board[currX][currY], Bishop):
                    break
                if (isinstance(self.board[currX][currY], Queen) or \
                    isinstance(self.board[currX][currY], Bishop)) and \
                    self.board[currX][currY].white != white:
                    return True

                currX += increment[0]
                currY += increment[1]
        print("past bishops / queens")
        # checks for pawns
        move = -1
        if white:
            move = 1

        for increment in [1, -1]:
            if 0 <= xPos + increment <= 7 and 0 <= yPos + move <= 7 and\
                isinstance(self.board[xPos + increment][yPos + move], Pawn) and \
                self.board[xPos + increment][yPos + move].white != white:
                return True
        print("past pawns")
        # checks for king
        moves = [(x + xPos, y + yPos, "N") for x in [1, 0, -1] for y in [1, 0, -1]]
        for move in moves:
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7 and \
                isinstance(self.board[move[0]][move[1]], King) and \
                self.board[move[0]][move[1]].white != white:
                return True
        print("past king")
        return False

    def select_piece(self, xPos, yPos):
        if not (0 <= xPos <= 7 and 0 <= yPos <= 7) or \
            self.board[xPos][yPos] is None or \
            self.board[xPos][yPos].white != self.turn:
            return False

        self.selected = self.board[xPos][yPos]
        return True

    def move(self, xPos, yPos):
        move = self.selected.move_piece(xPos, yPos, self.board)
        if move == None:
            return False

        # piece1 tells us (X, Y, selected) tells us selected is moved to X,Y
        piece1 = (xPos, yPos, self.selected)
        if move[2] == 'E':
            change = -1
            if self.turn:
                change = 1
            piece2 = (None, None, self.board[xPos][yPos + change])
            self.board[xPos][yPos] = self.selected
            self.board[xPos][yPos + change] = None
            self.board[self.selected.xPos][self.selected.yPos] = None

        elif move[2] == 'C':
            # check for checks before moving
            change = 1
            if move[0] < self.selected.xPos:
                change = -1
            for i in range(self.selected.xPos, move[0] + change, change):
                if self.contested(self.turn, i, yPos):
                    return False

            rookX = 7
            rookPos = 5
            if move[0] == 2:
                rookX = 0
                rookPos = 3

            piece2 = (rookPos, self.selected.yPos, self.board[rookX][self.selected.yPos])
            self.board[xPos][yPos] = self.selected
            self.board[self.selected.xPos][self.selected.yPos] = None
            self.board[rookPos][self.selected.yPos] = self.board[rookX][self.selected.yPos]
            self.board[rookX][self.selected.yPos] = None


        else:
            piece2 = (None, None, self.board[xPos][yPos])
            self.board[xPos][yPos] = self.selected
            self.board[self.selected.xPos][self.selected.yPos] = None


        # checks to see if king your king is put into check
        if move[2] != 'C':
            if (self.turn and self.contested(self.turn, self.white_king.xPos, self.white_king.yPos)) or \
                (not self.turn and self.contested(self.turn, self.black_king.xPos, self.black_king.yPos)):
                # rollback
                self.board[piece1[0]][piece1[1]] = None
                if piece2[0] is not None:
                    self.board[piece2[0]][piece2[1]] = None
                self.board[piece1[2].xPos][piece1[2].yPos] = piece1[2]
                if piece2[2] is not None:
                    self.board[piece2[2].xPos][piece2[2].yPos] = piece2[2]
                return False

        piece1[2].xPos = piece1[0]
        piece1[2].yPos = piece1[1]
        piece1[2].moved = True
        if piece2[2] is not None:
            piece2[2].xPos = piece2[0]
            piece2[2].yPos = piece2[1]
            piece2[2].moved = True


        self.turn = not self.turn
        return True
