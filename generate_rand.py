import random
import string

my_list = [1, 2, 3, "a", 2.0, 2.7, "stamp"]
print(random.random())  # Generates a random number between 0 and 1
print(random.randint(1, 10))  # Generate a random  integer between 1 and 10
print(random.choice(my_list))  # Randomly picks ONE item from my_list
print(random.choices(my_list,k=3))  # Randomly picks THREE item from my_list
generate_password = "".join(random.choices(string.ascii_letters + string.digits + "@!_", k=10))
print(generate_password)