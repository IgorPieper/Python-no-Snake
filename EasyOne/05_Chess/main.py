import pygame
import chess

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Szachy")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (186, 202, 68)
RED = (255, 0, 0)

# Wczytywanie grafik dla pionków
pieces = {
    "P": pygame.image.load("assets/white_pawn.png"),
    "N": pygame.image.load("assets/white_knight.png"),
    "B": pygame.image.load("assets/white_bishop.png"),
    "R": pygame.image.load("assets/white_rook.png"),
    "Q": pygame.image.load("assets/white_queen.png"),
    "K": pygame.image.load("assets/white_king.png"),
    "p": pygame.image.load("assets/black_pawn.png"),
    "n": pygame.image.load("assets/black_knight.png"),
    "b": pygame.image.load("assets/black_bishop.png"),
    "r": pygame.image.load("assets/black_rook.png"),
    "q": pygame.image.load("assets/black_queen.png"),
    "k": pygame.image.load("assets/black_king.png")
}

# Skalowanie pionków do rozmiaru pola
for key in pieces:
    pieces[key] = pygame.transform.scale(pieces[key], (SQUARE_SIZE, SQUARE_SIZE))

def draw_board(win, selected_square=None, valid_moves=None):
    colors = [WHITE, BLACK]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            if selected_square is not None and (row, col) == selected_square:
                color = HIGHLIGHT
            pygame.draw.rect(win, color, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            if valid_moves and (row, col) in valid_moves:
                pygame.draw.circle(win, HIGHLIGHT, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 10)

def draw_pieces(win, board):
    for row in range(8):
        for col in range(8):
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                win.blit(pieces[piece.symbol()], pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def get_square_under_mouse():
    mouse_pos = pygame.mouse.get_pos()
    col = mouse_pos[0] // SQUARE_SIZE
    row = mouse_pos[1] // SQUARE_SIZE
    return row, col

def promote_pawn(board, move):
    if board.piece_at(move.from_square).piece_type == chess.PAWN:
        if chess.square_rank(move.to_square) in [0, 7]:
            return chess.Move(move.from_square, move.to_square, promotion=chess.QUEEN)
    return move

def check_game_over(board):
    if board.is_checkmate():
        return "Checkmate! " + ("White wins!" if board.turn == chess.BLACK else "Black wins!")
    elif board.is_stalemate():
        return "Stalemate! It's a draw!"
    elif board.is_insufficient_material():
        return "Draw due to insufficient material!"
    elif board.is_seventyfive_moves():
        return "Draw due to 75-move rule!"
    elif board.is_fivefold_repetition():
        return "Draw due to fivefold repetition!"
    elif board.is_variant_draw():
        return "Draw!"
    return None

def display_message(win, message):
    font = pygame.font.Font(None, 72)
    text = font.render(message, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    win.blit(text, text_rect)
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    board = chess.Board()
    selected_square = None
    valid_moves = []
    game_over = False
    result_message = None

    run = True
    while run:
        clock.tick(30)
        draw_board(WIN, selected_square, valid_moves)
        draw_pieces(WIN, board)
        pygame.display.flip()

        if game_over:
            display_message(WIN, result_message)
            pygame.time.wait(3000)  # Czekaj 3 sekundy
            board = chess.Board()  # Resetowanie gry
            selected_square = None
            valid_moves = []
            game_over = False
            result_message = None
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                row, col = get_square_under_mouse()
                square = chess.square(col, 7 - row)

                if selected_square is None:  # Wybór pionka
                    piece = board.piece_at(square)
                    if piece and piece.color == board.turn:
                        selected_square = (row, col)
                        valid_moves = [(7 - move.to_square // 8, move.to_square % 8) for move in board.legal_moves if move.from_square == square]
                else:  # Wykonanie ruchu
                    move = chess.Move(chess.square(selected_square[1], 7 - selected_square[0]), square)
                    move = promote_pawn(board, move)
                    if move in board.legal_moves:
                        board.push(move)
                        result_message = check_game_over(board)
                        print(f"After move {move}, board state:\n{board}")
                        if result_message:
                            print(f"Game Over: {result_message}")
                            game_over = True
                            continue  # Zatrzymaj wykonywanie dalszych ruchów po zakończeniu gry
                    selected_square = None
                    valid_moves = []

    pygame.quit()

if __name__ == "__main__":
    main()
