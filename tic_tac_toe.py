import pygame
import sys


WIDTH, HEIGHT = 300, 300
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS
LINE_WIDTH = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def draw_grid():
    for row in range(1, ROWS):
        pygame.draw.line(WIN, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, COLS):
        pygame.draw.line(WIN, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'X':
                pygame.draw.line(WIN, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE), ((col + 1) * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
                pygame.draw.line(WIN, RED, ((col + 1) * SQUARE_SIZE, row * SQUARE_SIZE), (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(WIN, BLUE, ((col * SQUARE_SIZE) + SQUARE_SIZE//2, (row * SQUARE_SIZE) + SQUARE_SIZE//2), SQUARE_SIZE//2 - LINE_WIDTH//2, LINE_WIDTH)

def check_win(board, player):
    for row in range(ROWS):
        if all(board[row][col] == player for col in range(COLS)):
            return True

    for col in range(COLS):
        if all(board[row][col] == player for row in range(ROWS)):
            return True

    if all(board[i][i] == player for i in range(ROWS)):
        return True

    if all(board[i][ROWS-i-1] == player for i in range(ROWS)):
        return True

    return False

def check_draw(board):
    return all(board[row][col] != '-' for row in range(ROWS) for col in range(COLS))

def main():
    board = [['-' for _ in range(COLS)] for _ in range(ROWS)]
    turn = 'X'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not check_win(board, 'X') and not check_win(board, 'O') and not check_draw(board):
                x, y = pygame.mouse.get_pos()
                row, col = y // SQUARE_SIZE, x // SQUARE_SIZE

                if board[row][col] == '-':
                    board[row][col] = turn
                    if check_win(board, turn):
                        print(f"{turn} wins!")
                    elif check_draw(board):
                        print("It's a draw!")
                    else:
                        turn = 'X' if turn == 'O' else 'O'

        WIN.fill(WHITE)
        draw_grid()
        draw_board(board)
        pygame.display.update()



main()
pygame.quit()