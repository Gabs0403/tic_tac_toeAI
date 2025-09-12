from . import engine as engine

# Purpose: Start or reset a game with a fresh empty board, record difficulty, and set who moves first.
# Returns: game_state dictionary.
def create_board(difficulty, current_player, player_type):
    board = engine.make_empty_board()
    status = engine.compute_status(board)

    game_state = {
        "board": board,
        "current_player": current_player,
        "player_type": player_type,
        "difficulty": difficulty,
        "status": status
    }

    return game_state
