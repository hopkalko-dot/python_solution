import re

text = 'https://python.org, http://example.com/page, ftp://files.com'
print(re.findall(r'https?://[^\s,]+', text))
