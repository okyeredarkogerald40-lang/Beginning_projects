from pathlib import Path
import json

number = input("What's your favorite number?: ")

path = Path('favorite_number.json')
content = json.dumps(number)
path.write_text(content)

