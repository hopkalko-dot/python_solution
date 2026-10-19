import re

text = 'Это   строка    с     пробелами.   Текст   '
print(re.sub(r' +', ' ', text).strip())
