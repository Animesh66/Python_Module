import shutil
from pathlib import Path
import shutil

path = Path("my_path/movies.json")
source_file = path
target_file = Path("New Location")
shutil.copy(source_file, target_file)
new_path = Path()
for file in new_path.rglob("*.py"):  # recursively fine all the .py files as Generator object
    print(file)
print(path.exists())
print(path.is_file())
print(path.parent)
print(path.absolute())
print(path.parent.absolute())
print(path.home())
print(path.read_text())
print(path.read_bytes())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.with_name("movies.txt"))