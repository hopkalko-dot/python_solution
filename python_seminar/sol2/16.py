import re
from collections import Counter

levels = Counter()
err_users = set()

with open('logs.txt', encoding='utf-8') as f:
    for line in f:
        m = re.search(r'\b(INFO|WARNING|ERROR)\b', line)
        if m:
            levels[m.group(1)] += 1
        um = re.search(r'ERROR User (\d+)', line)
        if um:
            err_users.add(um.group(1))

for lvl in ['INFO', 'WARNING', 'ERROR']:
    print(lvl, levels[lvl])
print(sorted(err_users, key=int))
