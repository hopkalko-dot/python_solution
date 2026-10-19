from pathlib import Path

d = input('Каталог: ')
ext = input('Расширение: ')
if not ext.startswith('.'):
    ext = '.' + ext

p = Path(d)
if not p.exists():
    print('Каталог не найден')
else:
    for f in p.rglob('*' + ext):
        if f.is_file():
            print(f, f.stat().st_size)
