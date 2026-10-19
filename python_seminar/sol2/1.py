def analyze(path):
    lines = 0
    words = 0
    chars = 0
    max_len = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            lines += 1
            s = line.rstrip('\n\r')
            chars += len(line)
            words += len(s.split())
            if len(s) > max_len:
                max_len = len(s)
    print(lines, words, chars, max_len)

if __name__ == '__main__':
    analyze('sample.txt')
