
# Purpose: create and return a NEW empty 3x3 board (each cell is " ").
# Returns: 3x3 list of lists of str.
def make_empty_board():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    return board
    

# Purpose: check coordinate is within 0 & 2 for both row and col.
# Returns: True if in range; otherwise False.
def is_in_bounds(row, col):
    if 0 <= row < 3 and 0 <= col < 3:
        return True
        
    return False

# Purpose: check whether the target cell has no mark yet.
# Returns: True if board[row][col] == " "; otherwise False.
def is_empty(board, row, col):
    if board[row][col] == " ":
        return True
    
    return False

# Purpose: list all playable coordinates on the current board.
# Returns: list of (row, col) for every empty cell.
def legal_moves(board):
    moves = []

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                moves.append((row, col))
    
    return moves

# Purpose: place player's mark at (row, col) and return a NEW board. current_player is "X" or "O".
# Returns: new 3x3 board with that cell set to "X" or "O".
def place_mark(board, row, col, current_player):
    new_board = []
    for row_vals in board:
        new_row = row_vals[:]    
        new_board.append(new_row)

    new_board[row][col] = current_player

    return new_board


# Purpose: evaluate the board state after a move.
# Returns: "win(X)" | "win(O)" | "draw" | "in_progress".
def compute_status(board, current_player):
    pass
    
    

# Purpose: flip the current player token.
# Returns: "O" if player == "X", else "X".
def other_player(current_player):
    pass
