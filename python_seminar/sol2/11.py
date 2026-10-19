import re

text = open('logs.txt', encoding='utf-8').read()
users = set(re.findall(r'User\s+(\d+)', text))
errors = [line for line in text.splitlines() if line.startswith('ERROR')]
err_users = set(re.findall(r'ERROR\s+User\s+(\d+)', text))

print(sorted(users, key=int))
print(errors)
print(sorted(err_users, key=int))
