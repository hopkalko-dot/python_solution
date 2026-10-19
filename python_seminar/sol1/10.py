from functools import wraps

def log_cmd(func):
    @wraps(func)
    def wrapper(self, *a, **k):
        print('exec', type(self).__name__)
        return func(self, *a, **k)
    return wrapper

class Add:
    def __init__(self, v):
        self.v = v
    @log_cmd
    def execute(self, p):
        p.val += self.v

class Multiply:
    def __init__(self, v):
        self.v = v
    @log_cmd
    def execute(self, p):
        p.val *= self.v

class Subtract:
    def __init__(self, v):
        self.v = v
    @log_cmd
    def execute(self, p):
        p.val -= self.v

class Divide:
    def __init__(self, v):
        self.v = v
    @log_cmd
    def execute(self, p):
        if self.v == 0:
            print('div0')
            return
        p.val /= self.v

class Processor:
    def __init__(self):
        self.val = 0
        self.hist = []

    def run(self, cmd):
        parts = cmd.split()
        if not parts or parts[0] == 'exit':
            return False
        if parts[0] == 'history':
            print(self.hist)
            return True
        try:
            v = float(parts[1])
        except:
            return True
        cmds = {'add': Add, 'multiply': Multiply, 'subtract': Subtract, 'divide': Divide}
        if parts[0] in cmds:
            cmds[parts[0]](v).execute(self)
            self.hist.append((parts[0], v, self.val))
            print(self.val)
        return True

p = Processor()
while True:
    if not p.run(input()):
        break
