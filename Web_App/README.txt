# Rock-Paper-Scissors Game in Flask

#### Video Demo: https://youtu.be/Sj1txEocotY
#### Description:
This is a simple Rock-Paper-Scissors game built with Python and Flask. The game allows users to play against the computer, track scores, and reset scores.

The project demonstrates the integration of Flask for web development, Python for game logic, and pytest for testing functionality.

---

## Features
- Play Rock-Paper-Scissors against the computer.
- Track the scores of Wins, Losses, and Ties dynamically.
- Reset the scores at any time.
- Fully tested with `pytest` to ensure application robustness.

---

## Files

### `app.py`
The main application file that:
- Initializes the Flask app.
- Contains game logic, including determining the winner based on player and computer moves.
- Defines routes for playing the game and resetting scores.

### `templates/index.html`
The HTML template for the game interface. It dynamically displays:
- Buttons for selecting moves (Rock, Paper, Scissors).
- The game's result and scores.
- A reset button to clear scores.

### `tests/test_project.py`
Contains the test cases for the project, including:
- Testing the root route.
- Testing the game logic (player vs. computer moves).
- Testing the reset functionality.

### `requirements.txt`
Lists the Python dependencies required to run the project.
Flask==2.3.3
pytest==7.4.0
## Installation

1. Clone the repository:
   git clone https://github.com/talla-hub/project.git
   cd rock-paper-scissors-flask
