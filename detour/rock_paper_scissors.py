import random
import json
from pathlib import Path


def load_score():
  path = Path('score.json')
  if path.exists():
    contents = path.read_text()
    return json.loads(contents)
  else:
    score = {'wins': 0, 'draws': 0, 'losses': 0}
    contents = json.dumps(score)
    path.write_text(contents)
    return score

def save_score(score):
  path = Path('score.json')
  path.write_text(json.dumps(score))



score = load_score()
round_count = 0
options = ["rock", "paper", "scissors"]
print("----ROCK, PAPER, SCISSORS----")
while True:
  round_count += 1
  print(f"\n--- Round {round_count} ---")
  computer_move = random.choice(options)

  player_move = input("\nEnter move('rock', 'paper', 'scissors): ")
  if player_move not in options:
    print("Invalid move. Enter again")
  else:
    if player_move == computer_move:
      score['draws'] += 1
      print("Draw")
      
      
    elif player_move == "rock" and computer_move == "paper" or player_move == "paper" and computer_move == "scissors":
      score['losses'] += 1
      print("You lost")
      
      
    elif player_move == "rock" and computer_move == "scissors" or player_move == "scissors" and computer_move == "paper":
      score['wins'] += 1
      print("You won")
      
      

    elif player_move == "scissors" and computer_move == "rock":
      score['losses'] += 1
      print("Draw")
      

    print(f"The computer chose {computer_move}")
    print(f"Score -> wins: {score['wins']}, losses: {score['losses']}, draws: {score['draws']}")

    save_score(score)
  if round_count == 3:
    if score['wins'] > score['losses']:
      print("You won this set!")
    else:
      print("You lost this round")
    play_again = input("\nDo you want to play again?: ").strip().lower()
    if play_again != "yes" :
      print("Thanks for playing")
      break
    else:
      reset_choice = input("Do you want to reset your score to zero? (yes/no): ").strip().lower()
      if reset_choice == "yes":
          score = {'wins': 0, 'draws': 0, 'losses': 0}
          save_score(score)
          print("Scores have been successfully reset to zero!\n")
          round_count = 0
      else:
          print("Continuing with your saved score!\n")
