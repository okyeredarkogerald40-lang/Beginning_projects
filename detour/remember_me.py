from pathlib import Path
import json

path = Path('user.json')
if path.exists():
  contents = path.read_text()
  user = json.loads(contents)
  email = json.loads(contents)
  print(f"Welcome back, {user['username']}, {user['email']}")

else:
  username = input("What's your name?")
  email = input("What is your email address?: ")
  age = input("How old are you?: ")

  user_details = {'username': username, 'email': email, 'age': age}

  path = Path('user.json')
  contents = json.dumps(user_details)
  path.write_text(contents)

  print(user_details)


