from pathlib import Path

path = Path("my_path/movies.json")
print(path.exists())
print(path.is_file())
print(path.parent)
print(path.absolute())
print(path.parent.absolute())
print(path.home())
print(path.read_text())
print(path.is_dir())
print(path.name)
print(path.stem)
print(path.suffix)