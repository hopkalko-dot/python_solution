def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('Файл не найден')
    except PermissionError:
        print('Нет прав')
    except OSError as e:
        print('Ошибка:', e)
    return None
