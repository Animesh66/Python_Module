import json


with open("movies.json") as file:
    data = file.read()

movies = json.loads(data)
print(movies)
