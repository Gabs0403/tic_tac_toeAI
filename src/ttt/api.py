# Exposes the three functions the UI will call.
# When a move needs validating/applied, call the engine; when an AI choice is needed, call the AI.
# No game loop here, UI handles that.

# Main idea: Asks engine.py to validate/apply, or ai.py to pick.
