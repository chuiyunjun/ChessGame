import pygame

from board import Board

def create_board():
    window = pygame.display.set_mode((700, 700))
    chess_board = Board(window)

    return chess_board




def play():
    chess_board = create_board()
    selected = None
    while True:
        chess_board.draw_board()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                indexXpos = (pos[0] - 30) // 80
                indexYpos = (pos[1] - 30) // 80
                print(indexXpos, indexYpos)
                if selected is None:
                    selected = chess_board.get_item(indexXpos, indexYpos)
                    print(selected)

                else:
                    initalx = selected.xpos
                    initaly = selected.ypos

                    board = chess_board.get_board()
                    print(selected.possible_moves(board))
                    print(selected.xpos, selected.ypos)
                    if selected.move_piece(indexXpos, indexYpos, board):
                        board[selected.xpos][selected.ypos] = selected
                        board[initalx][initaly] = None
                    selected = None



if __name__ == '__main__':
    play()