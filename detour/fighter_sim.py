import msvcrt
import random

def start_game():
  enemy_hp = 100
  moves = ['P', 'S', 'K', 'B']
  enemy_move = random.choice(moves)
  hp = 100
  while True:
    print(f"HP: {hp}")
    move = input("Enter your move: ")
    if move == 'P' and enemy_move == 'B':
      enemy_hp -= 2
      print(f"HP: {enemy_hp}")
    elif move == 'K' and enemy_move == 'B':
      enemy_hp -= 10
      print(f"HP: {enemy_hp}")
    elif move == 'S' and enemy_move == 'B':
      enemy_hp -= 20
      print(f"HP: {enemy_hp}")
    else:
      print("Invalid Move.")





def main():
  print("-----Welcome to Fighter Simulator-----")
  print("Enter 'P' to punch, 'K' to kick, 'S' to use sword, 'B' to block")
  print("Press any key to start.")
  msvcrt.getch()
  start_game()