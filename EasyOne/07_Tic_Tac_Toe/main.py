import pygame
import sys
import random

pygame.init()

BACKGROUND_COLOR = (18, 18, 18)
LINE_COLOR = (50, 50, 50)
CIRCLE_COLOR = (0, 150, 136)
CROSS_COLOR = (239, 83, 80)
TEXT_COLOR = (255, 255, 255)

WIDTH = 300
GAME_HEIGHT = 300
LINE_WIDTH = 10

SCREEN = pygame.display.set_mode((WIDTH, GAME_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_ROWS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 1
game_over = False
difficulty = "2 Players"

def draw_lines():
    pygame.draw.line(SCREEN, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(SCREEN, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(SCREEN, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, GAME_HEIGHT), LINE_WIDTH)
    pygame.draw.line(SCREEN, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, GAME_HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(SCREEN, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == -1:
                pygame.draw.line(SCREEN, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(SCREEN, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def check_winner():
    global game_over
    for row in range(BOARD_ROWS):
        if sum(board[row]) == 3 or sum(board[row]) == -3:
            draw_winning_line(row, 0, row, BOARD_COLS - 1)
            game_over = True

    for col in range(BOARD_COLS):
        if sum(board[row][col] for row in range(BOARD_ROWS)) == 3 or sum(board[row][col] for row in range(BOARD_ROWS)) == -3:
            draw_winning_line(0, col, BOARD_ROWS - 1, col)
            game_over = True

    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][0] + board[1][1] + board[2][2] == -3:
        draw_winning_line(0, 0, BOARD_ROWS - 1, BOARD_COLS - 1)
        game_over = True

    if board[0][2] + board[1][1] + board[2][0] == 3 or board[0][2] + board[1][1] + board[2][0] == -3:
        draw_winning_line(0, BOARD_COLS - 1, BOARD_ROWS - 1, 0)
        game_over = True

    if game_over:
        pygame.display.update()
        pygame.time.wait(3000)
        show_menu()

    if check_draw():
        pygame.display.update()
        pygame.time.wait(3000)
        show_menu()

def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def draw_winning_line(row1, col1, row2, col2):
    x1 = col1 * SQUARE_SIZE + SQUARE_SIZE // 2
    y1 = row1 * SQUARE_SIZE + SQUARE_SIZE // 2
    x2 = col2 * SQUARE_SIZE + SQUARE_SIZE // 2
    y2 = row2 * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(SCREEN, LINE_COLOR, (x1, y1), (x2, y2), LINE_WIDTH)

def reset_game():
    global board, player, game_over
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False
    SCREEN.fill(BACKGROUND_COLOR)
    draw_lines()

def show_menu():
    global difficulty, SCREEN
    SCREEN = pygame.display.set_mode((WIDTH, GAME_HEIGHT))
    menu_running = True
    while menu_running:
        SCREEN.fill(BACKGROUND_COLOR)
        font = pygame.font.Font(None, 36)

        title_text = font.render("Select Difficulty", True, TEXT_COLOR)
        two_players_text = font.render("1. 2 Players", True, TEXT_COLOR)
        easy_text = font.render("2. Easy", True, TEXT_COLOR)
        hard_text = font.render("3. Hard", True, TEXT_COLOR)
        exit_text = font.render("4. Exit", True, TEXT_COLOR)

        title_y_pos = 50
        spacing = 50

        SCREEN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, title_y_pos))
        SCREEN.blit(two_players_text, (WIDTH // 2 - two_players_text.get_width() // 2, title_y_pos + spacing))
        SCREEN.blit(easy_text, (WIDTH // 2 - easy_text.get_width() // 2, title_y_pos + spacing * 2))
        SCREEN.blit(hard_text, (WIDTH // 2 - hard_text.get_width() // 2, title_y_pos + spacing * 3))
        SCREEN.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, title_y_pos + spacing * 4))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = "2 Players"
                    menu_running = False
                elif event.key == pygame.K_2:
                    difficulty = "Easy"
                    menu_running = False
                elif event.key == pygame.K_3:
                    difficulty = "Hard"
                    menu_running = False
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()

    SCREEN = pygame.display.set_mode((WIDTH, GAME_HEIGHT))
    reset_game()

def ai_move_easy():
    empty_spots = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if board[row][col] == 0]
    if empty_spots:
        row, col = random.choice(empty_spots)
        board[row][col] = -1

def ai_move_medium():
    def check_potential_win(player_value):
        for row in range(BOARD_ROWS):
            if board[row].count(player_value) == 2 and board[row].count(0) == 1:
                col = board[row].index(0)
                return (row, col)

        for col in range(BOARD_COLS):
            col_values = [board[row][col] for row in range(BOARD_ROWS)]
            if col_values.count(player_value) == 2 and col_values.count(0) == 1:
                row = col_values.index(0)
                return (row, col)

        diagonal1 = [board[i][i] for i in range(BOARD_ROWS)]
        if diagonal1.count(player_value) == 2 and diagonal1.count(0) == 1:
            idx = diagonal1.index(0)
            return (idx, idx)

        diagonal2 = [board[i][BOARD_COLS - 1 - i] for i in range(BOARD_ROWS)]
        if diagonal2.count(player_value) == 2 and diagonal2.count(0) == 1:
            idx = diagonal2.index(0)
            return (idx, BOARD_COLS - 1 - idx)

        return None

    move = check_potential_win(-1)
    if move:
        board[move[0]][move[1]] = -1
        return

    move = check_potential_win(1)
    if move:
        board[move[0]][move[1]] = -1
        return

    ai_move_easy()

SCREEN.fill(BACKGROUND_COLOR)
draw_lines()
show_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                draw_figures()
                pygame.display.update()
                check_winner()

                if difficulty == "Easy" and player == 1 and not game_over:
                    ai_move_easy()
                elif difficulty == "Hard" and player == 1 and not game_over:
                    ai_move_medium()

                draw_figures()
                pygame.display.update()
                check_winner()

                if difficulty == "2 Players":
                    player *= -1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    pygame.display.update()
