import json

with open('students.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

best = None
best_score = -1
for s in data:
    score = s.get('score', 0)
    s['passed'] = score >= 60
    if score > best_score:
        best_score = score
        best = s.get('name')

print(best, best_score)

with open('students_new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
