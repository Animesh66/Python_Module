import json
from pathlib import Path

new_list = ["1", "2", "3", "4"]
movies = [{"id": 1, "name": "Terminator", "year": 1984}, {"id": 2, "name": "Harry Potter", "year": 2002}]

data = json.dumps(movies)  # Converts Python readable data to JSON file
path = Path("movies.json")
path.write_text(data)  # Creates a JSON file named movies.json
print("".join(new_list))
