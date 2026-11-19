from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
  content = path.read_text()
  number = json.loads(content)
  print(f"I know your favorite number. It is {number}")

else:
  number = input("What's your favorite number?: ")
  path = Path('favorite_number.json')
  content = json.dumps(number)
  path.write_text(content)
  print(f"I know your favorite number. It is {number}")