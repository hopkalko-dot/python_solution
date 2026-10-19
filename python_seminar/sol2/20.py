import re

text = '15.09.2026, 21.09.2026 и 03.10.2026. 1.11.2026'
print(re.findall(r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', text))
