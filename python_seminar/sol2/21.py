import re

def is_valid_login(login):
    if not 4 <= len(login) <= 16:
        return False
    return bool(re.match(r'^[A-Za-z][A-Za-z0-9_]*$', login))

print(is_valid_login('user_123'))
print(is_valid_login('123user'))
