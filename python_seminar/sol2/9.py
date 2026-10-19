def parse_number(value):
    return float(value)

s = input()
try:
    print(parse_number(s))
except ValueError:
    print('Ошибка')
