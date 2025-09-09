
Tic-Tac-Toe Engine Interface.


Shared Data (applies to all methods)
1. Players: "X" and "O".
2. Board: a 3x3 grid with cells that can be empty, "X", or "O".
3. game_status: in_progress (continue game loop), win(X), win(O), draw, illegal move.
4. game_state: current board state, whose turn it is (player or AI), chosen difficulty (picks correct algorithm for AI).

The idea is that UI will render everything that is in game state.

========================================================================================================
METHOD 1
create_board(difficulty, first_player) -> (game_state)
========================================================================================================

Purpose: Start or reset a game with a fresh empty board, record difficulty, and set who moves first.

Parameters (Required from front-end)
1. difficulty: "easy" or "impossible" to call the correct AI algorithm.
2. first_player: Needed to know who starts the game and which symbol the user picks "X" or "O".

Responsibilities (back-end)
1. Create an empty board (3x3 matrix of rows and columns).
2. Store the chosen difficulty in the Game State container (dictionary).
3. Set the "current player" to first_player.
4. Set game status to "in-progress".

Output (return value to front-end)
It will return the game_state with the following details:
1. empty 3x3 board.
2. current_player = first_player.
3. difficulty = difficulty.
4. set game_status to "in-progress".

========================================================================================================
METHOD 2
apply_move(game_state, row, col) -> (updated_game_state, status)
========================================================================================================

Purpose: place the current player's mark at the requested cell, if legal, update turn, and evaluate the game_status (win/lose/draw/in_progress). It enforces the rules.

Parameters (Required from front-end)
1. game_state: the most recent state back-end gave to UI. The front-end must keep the latest game_state back-end returned and pass that same object back to back-end on the next call.
2. row, col: the selection of the human player in the form of integers [0,2], indicating the tapped cell.

Responsibilities (back-end)
1. Validate the request: ensures the game is in-progress, row/col within bounds, target cell is empty.
2. If request legal: set the tapped cell to the current player's mark, check for a win (if not win checks for a draw), updates game_status, switches current player.
3. if request illegal: Does not modify board or current player, returns unchanged game_state, status set to illegal_move.
4. Return the new/unchanged game_state and the new status.
5. No moves allowed after a win/draw.
6. A cell cannot be overwritten.
7. Win detection covers all 8 lines.

Output (return value to front-end)
1. updated_game_state if move legal.
2. updated status.

========================================================================================================
METHOD 3
ai_move(game_state) -> (row, col)
========================================================================================================

Purpose: selects a legal move for the current player based on the game's difficulty.

Parameters (Required from front-end)
1. game_state: game_state after the human player last move (or at the start if AI goes first).

Responsibilities (back-end)
1. Read the stored difficulty from game_state.
2. if the status is not in_progress (already won/draw), indicate no move available (use a flag) and returns None.
3. if in_progress:
   - Easy: choose a quick/random legal move.
   - Impossible: choose optimal move to win.
4. Guarantee that the row and col returned is a legal/empty cell.

Output (return value to front-end)
1. (row, col): The AI's chosen move.
2. No move available: returns None.

========================================================================================================
game_state example schema
========================================================================================================
game_state = {
  "board": 3×3 grid of [" ", "X", "O"],
  "current_player": "X" or "O",
  "difficulty": "easy" or "impossible",
  "status": "in_progress" | "win(X)" | "win(O)" | "draw"
}


