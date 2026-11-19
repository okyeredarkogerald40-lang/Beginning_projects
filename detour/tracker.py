import json
from pathlib import Path


path = Path('expenses.json')
def load_expenses():
  if path.exists():
    contents = path.read_text()
    return json.loads(contents)
  else:
    return []

def save_expenses(tasks):
  content = json.dumps(tasks, indent=4)
  path.write_text(content)

def main():
  expenses = load_expenses()

  while True:
    print("\n1. View Expenses")
    print("2. Add Expenses")
    print("3. Delete Expenses")
    print("4. Exit")
    choice = input("What do you want to do?: ")

    
 
