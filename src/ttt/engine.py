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
    new_board = copy_board(board)
    new_board[row][col] = current_player

    return new_board


# Purpose: evaluate the board state after a move.
# Returns: "win(X)" | "win(O)" | "draw" | "in progress".
def compute_status(board):
    # Empty spot in the board
    EMPTY = " "

    # ===ROWS===
    for row in range(3):
        a, b, c = board[row][0], board[row][1], board[row][2]
        if a != EMPTY and a == b == c:
            status = f"win({a})"
            return status

    # ===COLUMNS===
    for col in range(3):
        a, b, c = board[0][col], board[1][col], board[2][col]
        if a != EMPTY and a == b == c:
            status = f"win({a})"
            return status

    # ===DIAGONAL===
    a, b, c = board[0][2], board[1][1], board[2][0]
    if a != EMPTY and a == b == c:
        status = f"win({a})"
        return status

    a, b, c = board[0][0], board[1][1], board[2][2]
    if a != EMPTY and a == b == c:
        status = f"win({a})"
        return status

    # ===Check if board full===
    if len(legal_moves(board)) == 0:
        status = "draw"
        return status
    else:
        status = "in progress"
        return status

# Purpose: flip the current player token.
# Returns: "O" if player == "X", else "X".
def other_player(current_player):
    if current_player == "X":
        current_player = "O"
        return current_player
    else:
        current_player = "X"
        return current_player


# Purpose: creates game_state dictionary.
# Returns: a new game_state dictionary.
def new_game_state(prev_game_state, row, col):
    game_state = {}

    board = prev_game_state["board"]
    current_player = prev_game_state["current_player"]
    difficulty = prev_game_state["difficulty"]
    status = prev_game_state["status"]

    if status == "in progress" or status == "illegal move":
        if is_in_bounds(row, col) and is_empty(board, row, col):
            game_state["board"] = place_mark(board, row, col, current_player)
            game_state["difficulty"] = difficulty
            game_state["status"] = compute_status(game_state["board"])
            if game_state["status"] == "in progress":
                game_state["current_player"] = other_player(current_player)
            else:
                game_state["current_player"] = current_player
        else:

            game_state["board"] = copy_board(board)
            game_state["current_player"] = current_player
            game_state["difficulty"] = difficulty
            game_state["status"] = "illegal move"

    return game_state

# Purpose: Copy existing board.
# Returns: Copy of the current board.
def copy_board(board):
    new_board = []
    for row_vals in board:
        new_row = row_vals[:]
        new_board.append(new_row)

    return new_board
