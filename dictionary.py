import os
my_dict = {"id": 1, "name": "Terminator", "year": 1984}

for value in my_dict.items():
    print(value)
print(os.getenv("DB_PWD"))