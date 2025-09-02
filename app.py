
import random
from flask import Flask, jsonify, render_template, request

# Game constants
WIDTH = 10
HEIGHT = 20
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

# Game state
board = [[0] * WIDTH for _ in range(HEIGHT)]
current_piece = None
current_pos = [0, 0]
score = 0
game_over = False

def new_piece():
    """Create a new random piece."""
    global current_piece, current_pos
    shape = random.choice(SHAPES)
    current_piece = shape
    current_pos = [0, WIDTH // 2 - len(shape[0]) // 2]

def check_collision(piece, pos):
    """Check for collision with board boundaries or other pieces."""
    for r, row in enumerate(piece):
        for c, cell in enumerate(row):
            if cell:
                board_r, board_c = pos[0] + r, pos[1] + c
                if (board_r >= HEIGHT or
                        board_c < 0 or
                        board_c >= WIDTH or
                        board[board_r][board_c]):
                    return True
    return False

def lock_piece():
    """Lock the current piece onto the board."""
    global board
    for r, row in enumerate(current_piece):
        for c, cell in enumerate(row):
            if cell:
                board[current_pos[0] + r][current_pos[1] + c] = 1
    clear_lines()

def clear_lines():
    """Clear completed lines and update the score."""
    global board, score
    new_board = [row for row in board if not all(row)]
    lines_cleared = HEIGHT - len(new_board)
    score += lines_cleared * 100
    board = [[0] * WIDTH for _ in range(lines_cleared)] + new_board

def move(dx, dy):
    """Move the current piece."""
    global current_pos, game_over
    new_pos = [current_pos[0] + dy, current_pos[1] + dx]
    if not check_collision(current_piece, new_pos):
        current_pos = new_pos
        return True
    else:
        if dy > 0: # If moving down and collision
            lock_piece()
            new_piece()
            if check_collision(current_piece, current_pos):
                game_over = True
        return False

def rotate():
    """Rotate the current piece."""
    global current_piece
    rotated_piece = [list(row) for row in zip(*current_piece[::-1])]
    if not check_collision(rotated_piece, current_pos):
        current_piece = rotated_piece

def reset_game():
    """Reset the game state."""
    global board, score, game_over
    board = [[0] * WIDTH for _ in range(HEIGHT)]
    score = 0
    game_over = False
    new_piece()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    reset_game()
    return jsonify(get_game_state())

@app.route('/gamestate')
def gamestate():
    return jsonify(get_game_state())

@app.route('/move', methods=['POST'])
def move_piece():
    direction = request.json.get('direction')
    if direction == 'left':
        move(-1, 0)
    elif direction == 'right':
        move(1, 0)
    elif direction == 'down':
        move(0, 1)
    elif direction == 'rotate':
        rotate()
    return jsonify(get_game_state())

def get_game_state():
    """Get the current game state."""
    # Create a temporary board to show the current piece
    temp_board = [row[:] for row in board]
    if current_piece:
        for r, row in enumerate(current_piece):
            for c, cell in enumerate(row):
                if cell:
                    temp_board[current_pos[0] + r][current_pos[1] + c] = 2 # Use 2 for the moving piece
    return {
        'board': temp_board,
        'score': score,
        'game_over': game_over
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
