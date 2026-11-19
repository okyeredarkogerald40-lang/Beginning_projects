import msvcrt
quiz_questions = [
    {
        "question": "What is the longest river in the world?",
        "options": ["A) Amazon River", "B) Nile River", "C) Mississippi River", "D) Yangtze River"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold on the periodic table?",
        "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
        "answer": "C"
    },
    {
        "question": "In what year did the Titanic sink in the Atlantic Ocean?",
        "options": ["A) 1905", "B) 1912", "C) 1918", "D) 1923"],
        "answer": "B"
    },
    {
        "question": "Which planet in our solar system has the most moons?",
        "options": ["A) Jupiter", "B) Mars", "C) Neptune", "D) Saturn"],
        "answer": "D"
    },
    {
        "question": "What is the only mammal capable of true, sustained flight?",
        "options": ["A) Flying Squirrel", "B) Bat", "C) Sugar Glider", "D) Eagle"],
        "answer": "B"
    },
    {
        "question": "Who painted the famous masterpiece The Mona Lisa?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"],
        "answer": "C"
    },
    {
        "question": "Which country has the most natural lakes in the world?",
        "options": ["A) Canada", "B) Russia", "C) United States", "D) Finland"],
        "answer": "A"
    },
    {
        "question": "What gas makes up the majority of Earth's atmosphere?",
        "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"],
        "answer": "C"
    },
    {
        "question": "What is the highest-grossing film worldwide of all time?",
        "options": ["A) Avengers: Endgame", "B) Avatar", "C) Titanic", "D) Star Wars: The Force Awakens"],
        "answer": "A"
    },
    {
        "question": "What internal human organ can regenerate or repair itself completely?",
        "options": ["A) Heart", "B) Kidney", "C) Lungs", "D) Liver"],
        "answer": "D"
    }
]



def start_game():
  correct_answers = 0
  for question in quiz_questions:
    print(question["question"])

    for option in question["options"]:
      print(option)
    while True:
        answer = input("Enter your answer: ")
        valid_options = ["A", "B", "C", "D"]
        if answer.upper() in valid_options:
          if answer.upper() == question["answer"]:
            correct_answers += 1
          break
        else:
          print("Invalid answer. Try again")
  
  if correct_answers <= 4:
    print(f"Try harder next time. You scored {correct_answers} out of 10")
  elif correct_answers >= 5 and correct_answers <= 7:
    print(f"Well done.  You scored {correct_answers} out of 10")
  elif correct_answers >= 8:
    print(f"Excellent!  You scored {correct_answers} out of 10")


def main():
  print("Welcome to GILLY'S TRIVIA. Press any key to start.")
  msvcrt.getch()
  print("\nKey detected! Let's start the quiz....\n")
  start_game()
  
if __name__ == "__main__":
  main()

