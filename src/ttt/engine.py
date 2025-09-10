# ==================================================================== 
# Enforces rules (the referee) of the moves/game.
# ==================================================================== 

# Purpose: create and return a NEW empty 3x3 board (each cell is " ").
# Returns: 3x3 list of lists of str.
def make_empty_board():
    pass

# Purpose: check coordinate is within 0..2 for both row and col.
# Returns: True if in range; otherwise False.
def is_in_bounds(row, col):
    pass

# Purpose: check whether the target cell has no mark yet.
# Returns: True if board[row][col] == " "; otherwise False.
def is_empty(board, row, col):
    pass

# Purpose: list all playable coordinates on the current board.
# Returns: list of (row, col) for every empty cell.
def legal_moves(board):
    pass

# Purpose: place player's mark at (row, col) and return a NEW board.
# Returns: new 3x3 board with that cell set to "X" or "O".
def place_mark(board, row, col, player):
    pass

# Purpose: evaluate the board state after a move.
# Returns: "win(X)" | "win(O)" | "draw" | "in_progress".
def compute_status(board):
    pass

# Purpose: flip the current player token.
# Returns: "O" if player == "X", else "X".
def other_player(player):
    pass
