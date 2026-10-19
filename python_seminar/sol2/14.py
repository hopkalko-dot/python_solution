from contextlib import contextmanager

@contextmanager
def log_operation(path, name):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f'START: {name}\n')
        try:
            yield
            f.write(f'END: {name}\n')
        except Exception:
            f.write(f'ERROR: {name}\n')
            raise

with log_operation('op.log', 'test'):
    print('ok')
