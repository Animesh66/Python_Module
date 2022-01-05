import json
from pprint import pprint
from pathlib import Path

data = Path("movies.json").read_text()
# with open("movies.json") as file:
#     data = file.read()

movies = json.loads(data)  # converts JSON file to Python readable format
pprint(movies)
pprint(movies[0]['name'])
