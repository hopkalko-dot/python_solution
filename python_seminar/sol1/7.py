import re
from collections import defaultdict

def word_count(path):
    counts = defaultdict(int)
    with open(path, encoding='utf-8') as f:
        for line in f:
            for w in re.findall(r"[A-Za-zА-Яа-яёЁ0-9']+", line.lower()):
                counts[w] += 1
    top = sorted(counts.items(), key=lambda x: -x[1])[:10]
    for w, c in top:
        print(w, c)

word_count('text.txt')
