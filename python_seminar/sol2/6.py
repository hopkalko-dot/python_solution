from pathlib import Path

p = Path('.')
files = 0
dirs = 0
py = []
size = 0

for item in p.rglob('*'):
    if item.is_file():
        files += 1
        size += item.stat().st_size
        if item.suffix == '.py':
            py.append(str(item))
    elif item.is_dir():
        dirs += 1

print(files)
print(dirs)
print(py)
print(size)
