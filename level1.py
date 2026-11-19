from random import randint

print("Welcome to this number guessing game")
computerNum = randint(1, 10)
guess_count = 0
guessing = False

while not guessing:
  try:
    guess = int(input("Guess any number between from 1 to 10: "))
    guess_count += 1
    if guess < computerNum:
      print(f"Too low. Try again. Guesses: {guess_count}")
    elif guess > computerNum:
      print(f"Too high. Try again. Guesses: {guess_count}")
    else:
      print(f"Correct guess! Well done. It took you {guess_count} guesses.")
      guessing = True
  except ValueError:
    print("Please enter a valid number.")

    
  