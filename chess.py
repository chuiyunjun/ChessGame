import pygame

from board import Board

def create_board():
	window = pygame.display.set_mode((700, 700))
	chess_board = Board(window)

	return chess_board




def play():
	chess_board = create_board()
	while True:
		chess_board.draw_board()


if __name__ == '__main__':
	play()