import json
from pathlib import Path

movies = [{"id": 1, "name": "Terminator", "year": 1984}, {"id": 2, "name": "Harry Potter", "year": 2000}]

data = json.dumps(movies)  # converts python data to json
path = Path("movies.json")
path.write_text(data)  # create a json file
