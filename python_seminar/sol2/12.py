import re

text = '''alice@example.com
bob@test.org
alice@example.com
admin@company.ru'''

emails = re.findall(r'\b[\w.%+-]+@[\w.-]+\.\w{2,}\b', text)
seen = []
for e in emails:
    if e not in seen:
        seen.append(e)
print('\n'.join(seen))
