# Tic Tac Toe Game Flow

## 1. Starting the Game
- The **UI** creates an empty 3×3 board (all spaces blank).  
- The UI calls the backend’s **`create_board(difficulty, first_player)`** method.  
- The **backend** validates that the board is correct:
  - Must be 3×3 shape.  
  - Only legal values allowed (`"X"`, `"O"`, `" "`).  
  - No illegal advantage (e.g., too many X’s).  
- The backend returns a **game_state** object containing:
  - the board,  
  - the chosen difficulty,  
  - which player goes first,  
  - the game status (`in_progress`).

---

## 2. Checking Whose Turn It Is
- If it’s the **human’s turn**, the UI waits for a tap.  
- If it’s the **AI’s turn**, the UI immediately calls **`ai_move(game_state)`**.

---

## 3. Human Move Flow
- Player taps a cell on the touchscreen.  
- The UI calls **`apply_move(game_state, row, col)`**.  
- The **backend**:
  - Checks if the move is legal (inside bounds, empty cell, game not over).  
  - Updates the board with the move.  
  - Switches to the next player.  
  - Evaluates the new status:
    - `in_progress` → continue the loop.  
    - `win(X)`, `win(O)`, or `draw` → stop the game.  
    - `illegal_move` → ignore and stay on the same turn.

---

## 4. AI Move Flow
- When it’s the AI’s turn, the UI calls **`ai_move(game_state)`**.  
- The **backend** uses the stored difficulty to decide:
  - **Easy** → pick a random legal move.  
  - **Impossible** → run the optimal algorithm (minimax).    
- The backend applies the move, updates the board, switches turns, and evaluates status.
- The backend returns an updated `game_state` with the AI's choice. 

---

## 5. Repeating the Loop
- After **every move**, the backend always returns a fresh `game_state`.  
- The **UI** replaces its copy of the state with the new one.  
- The cycle continues:
  - Check whose turn.  
  - Handle human or AI move.  
  - Apply move and update state.  
- The loop ends only when the backend reports a final status: **win, draw, or illegal move**.

---

## Responsibilities
- **UI (Frontend):** handles touch input, calls backend functions, maintains game loop and redraws the board.  
- **Backend:** enforces rules, updates the state, decides AI moves, and declares the result.

