from pathlib import Path
import json

path = Path('tasks.json')

def load_tasks():
  """Loads tasks from file if it exists"""
  if path.exists():
    content = path.read_text()
    return json.loads(content)
  return []

def save_tasks(tasks):
  """Saves tasks to the file"""
  content = json.dumps(tasks, indent=4)
  path.write_text(content)

def main():
  tasks = load_tasks()

  while True:
    print("\n---TO-DO LIST---")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Check-off Tasks")
    print("4. Uncheck Tasks")
    print("5. Delete Tasks")
    print("6. Exit")
    choice = input("What do you want to do? ")
    
    if choice == "1":
      if len(tasks) == 0:
        print("\nYour to-do list is empty")
      else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
          task = tasks[i]
          if task['completed'] == True:
            status = "[X]"
          else:
            status = "[]"
          print(f"{i + 1}. {status} {task['title']}")
    elif choice == "2":
      while True:
        title = input("Enter your task description: ")
        if title == "q":
          print("Exiting task addition..")
          break
        new_task = {'title': title, 'completed': False}
        tasks.append(new_task)
        print("Task added successfully")
        
    elif choice == "3":
      for i in range(len(tasks)):
        task = tasks[i]
        if task['completed'] == True:
                    status = "[X]"
        else:
          status = "[]"
        print(f"{i + 1}. {status} {task['title']}")
       
      while True:
        option = int(input("Which task do you want to check-off?: "))
        if option == 00:
          break
        index = option - 1
        if index >= 0 and index < len(tasks):
          tasks[index]['completed'] = True
          save_tasks(tasks)
          print("Task successfully checked-off")

    elif choice == "4":
      for i in range(len(tasks)):
        task = tasks[i]
        if task['completed'] == True:
          status = "[X]"
        else:
          status = "[]"
        print(f"{i + 1}. {status} {task['title']}")
             
      while True:
        option = int(input("Which task do you want to uncheck?: "))
        if option == 00:
          break
        index = option - 1
        if index >= 0 and index < len(tasks):
          tasks[index]['completed'] = False
          save_tasks(tasks)
          print("Task successfully unchecked")
    elif choice == "5":
      for i in range(len(tasks)):
        task = tasks[i]
        if task['completed'] == True:
          status = "[X]"
        else:
          status = "[]"
        print(f"{i + 1}. {status} {task['title']}")
      while True:
        choice = int(input("Which task do you want to delete?: "))
        if choice == 00:
          break
        index = choice - 1
        if index >= 0 and index < len(tasks):
          removed = tasks.pop(index) 
          print(f"{removed['title']} successfully removed")
      
    elif choice == "6":
      print("Exiting To-do list. Goodbye")
      break 
    else:
      print("Invalid choice. Enter choice again")

if __name__ == "__main__":
  main()


    
      





    



  




