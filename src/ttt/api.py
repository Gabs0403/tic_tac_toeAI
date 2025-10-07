from . import engine as engine

# Purpose: Start or reset a game with a fresh empty board, record difficulty, and set who moves first.
# Returns: game_state dictionary.


def create_board(difficulty, current_player, current_type):
    board = engine.make_empty_board()
    status = engine.compute_status(board)

    game_state = {
        "board": board,
        "current_player": current_player,
        "difficulty": difficulty,
        "status": status,
        "current_type": current_type
    }

    return game_state

# Purpose: Place the current player's mark at the requested cell.
# Returns: updated game_state.


def human_move(game_state, row, col):
    return engine.new_game_state(game_state, row, col)

# Purpose: Select a legal move for the AI based on the game’s difficulty.
# Returns: updated game_state.


def ai_move(game_state):
    difficulty = game_state["difficulty"]

    if difficulty == "Easy":
        return engine.ai_easy(game_state)
    return engine.ai_impossible(game_state)
