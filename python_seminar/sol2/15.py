from io import StringIO

def count_lines(stream):
    n = 0
    for _ in stream:
        n += 1
    return n

print(count_lines(open('sample.txt', encoding='utf-8')))
print(count_lines(StringIO('a\nb\nc\n')))
