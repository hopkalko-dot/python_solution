import re

pat = re.compile(r'(?P<dt>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>INFO|WARNING|ERROR) User (?P<uid>\d+) (?P<msg>.+)')

logs = [
    '2026-09-24 10:15:32 INFO User 123 logged in',
    '2026-09-24 10:16:04 ERROR User 456 authentication failed',
]

for line in logs:
    m = pat.match(line)
    if m:
        print(m.groupdict())
