import tkinter as tk
import random

# 1. Initialize the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x350")

# 2. Create a label to display game results and scores
result_label = tk.Label(root, text="Welcome! Choose your move below:", font=("Arial", 12))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Wins: 0 | Losses: 0 | Draws: 0", font=("Arial", 10, "bold"))
score_label.pack(pady=10)

# Track scores in memory for this session
scores = {"wins": 0, "losses": 0, "draws": 0}

# 3. Define the game logic function linked to the buttons
def play(player_move):
    options = ["rock", "paper", "scissors"]
    computer_move = random.choice(options)
    
    # Evaluate winner
    if player_move == computer_move:
        scores["draws"] += 1
        outcome = "It's a Draw!"
    elif (player_move == "rock" and computer_move == "paper") or \
         (player_move == "paper" and computer_move == "scissors") or \
         (player_move == "scissors" and computer_move == "rock"):
        scores["losses"] += 1
        outcome = "You Lost!"
    else:
        scores["wins"] += 1
        outcome = "You Won!"
        
    # Update the window labels with the results
    result_label.config(text=f"{outcome}\nYou chose: {player_move}\nComputer chose: {computer_move}")
    score_label.config(text=f"Wins: {scores['wins']} | Losses: {scores['losses']} | Draws: {scores['draws']}")

# 4. Create clickable buttons for the player
btn_rock = tk.Button(root, text="Rock", width=15, bg="lightgray", command=lambda: play("rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", width=15, bg="lightgray", command=lambda: play("paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", width=15, bg="lightgray", command=lambda: play("scissors"))
btn_scissors.pack(pady=5)

# 5. Run the application loop
root.mainloop()