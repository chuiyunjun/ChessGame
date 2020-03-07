import pygame

from board import Board

def create_board():
    window = pygame.display.set_mode((700, 700))
    chess_board = Board(window)

    return chess_board




def play():
    chess_board = create_board()
    selected = False
    while True:
        chess_board.draw_board()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                indexXpos = (pos[0] - 30) // 80
                indexYpos = (pos[1] - 30) // 80
                if not selected:
                    selected = chess_board.select_piece(indexXpos, indexYpos)

                else:
                    moved = chess_board.move(indexXpos, indexYpos)
                    selected = False


if __name__ == '__main__':
    play()