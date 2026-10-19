import csv
from collections import defaultdict

scores = []
groups = defaultdict(list)
best = ''
best_score = -1

with open('students.csv', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            s = float(row['score'])
            scores.append(s)
            groups[row['group']].append(s)
            if s > best_score:
                best_score = s
                best = row['name']
        except:
            pass

if scores:
    print(sum(scores) / len(scores))
    print(best, best_score)
    for g, lst in groups.items():
        print(g, sum(lst) / len(lst))
