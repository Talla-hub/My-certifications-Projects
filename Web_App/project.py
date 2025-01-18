from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Initialize scores globally
scores = {
    "Wins": 0,
    "Loses": 0,
    "Ties": 0
}

# Function to generate computer's move
def computer_move():
    moves = ["rock", "paper", "scissors"]
    return random.choice(moves)

# Function to play the game
def play_game(player_move):
    global scores
    computer_move_value = computer_move()
    
    if computer_move_value == "paper" and player_move == "rock":
        scores["Loses"] += 1
        result = "You lose!!!"
    elif computer_move_value == "scissors" and player_move == "rock":
        scores["Wins"] += 1
        result = "You win!!!"
    elif computer_move_value == "scissors" and player_move == "paper":
        scores["Loses"] += 1
        result = "You lose!!!"
    elif computer_move_value == "rock" and player_move == "paper":
        scores["Wins"] += 1
        result = "You win!!!"
    elif computer_move_value == "rock" and player_move == "scissors":
        scores["Loses"] += 1
        result = "You lose!!!"
    elif computer_move_value == "paper" and player_move == "scissors":
        scores["Wins"] += 1
        result = "You win!!!"
    else:
        scores["Ties"] += 1
        result = "It's a tie!!!"
    
    return result, computer_move_value

# Route for the game page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the player's move from the form
        player_move = request.form.get("move")
        
        # Play the game and get the result
        result, computer_move_value = play_game(player_move)
        
        # Render the game page with the updated scores and result
        return render_template(
            'index.html', 
            scores=scores, 
            result=result, 
            player_move=player_move.title(), 
            computer_move=computer_move_value.title()
        )
    
    # On GET request (initial load), render the page with current scores
    return render_template('index.html', scores=scores)

# Route to reset the game scores
@app.route('/reset', methods=["POST"])
def reset():
    global scores
    scores = {
        "Wins": 0,
        "Loses": 0,
        "Ties": 0
    }
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
