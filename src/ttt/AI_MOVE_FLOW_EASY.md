# AI_MOVE_EASY_V1.md

## Purpose
Define the **Easy** AI: pick a move **uniformly at random** from the current legal moves and return a **new `game_state`** with that move applied.  
This is for a quick demo and can be improved later to make it less "dumb".

---

## Contract

**Input:**  
- `game_state` with:
  - `board` (3×3 grid using `" "` for empty),
  - `current_player` (`"X"` or `"O"`),
  - `current_type` (`"human"` or `"AI"`),
  - `difficulty`,
  - `status` (`"in progress"` or `"illegal move"` in this scheme).

**Output:**  
- A **new `game_state`** snapshot:
  - If no move should be made: return an **unchanged snapshot**.

---

## Core Algorithm (flow-in-words)

1. **Collect legal moves**  
   - Read the board and build the list of empty `(row, col)` positions.

2. **Choose uniformly at random**  
   - Pick exactly one move from that list with equal probability.

3. **Apply the move via the `place_mark(board, row, col, current_type)`**  
   - Feed `(row, col)` and the *current* `game_state` into `place_mark(board, row, col, current_type)` (the same logic used for human moves).  
   - This produces a **new `game_state`** where:
     - The selected cell contains `current_player`’s mark,
     - `status` is recomputed (`"win(X)" | "win(O)" | "draw" | "in progress"`),
     - `current_player` flips **only if** the new status is `"in progress"`,
     - `current_type` flips **only if** the new status is `"in progress"` (e.g., `"AI" → "human"`); otherwise it stays as `"AI"` in terminal states.

4. **Return the new snapshot**  
   - Hand the updated `game_state` back to the caller (UI).

---

## Pseudo-Flow (textual “flowchart”)

- **Start**  
  ↓  
- Read `status`  
  - If **not** `"in progress"` → **Return unchanged state**  
  - Else continue  
  ↓  
- Check `current_type`  
  - If **not** `"AI"` → **Return unchanged state**  
  - Else continue  
  ↓  
- Compute `legal_moves`  
  - If **none** → **Return unchanged state**  
  - Else continue  
  ↓  
- **Randomly select** one `(row, col)` from `legal_moves`  
  ↓  
- **Apply** the move (use the reducer to get a fresh `game_state`)  
  - If new `status` is `"in progress"` → flip `current_player` **and** set `current_type = "human"`  
  - Else (win/draw) → keep `current_player` and `current_type` as they were  
  ↓  
- **Return** the new `game_state`

---

## Edge Cases

- **Stale/terminal call:** If invoked after a win/draw or with `status = "illegal move"`, it returns the **unchanged** state.  
- **Wrong role:** If called when `current_type != "AI"`, returns unchanged state (defensive).  
- **Full board:** No legal moves → unchanged state.  
- **Single legal move:** That move is selected with probability 1.
