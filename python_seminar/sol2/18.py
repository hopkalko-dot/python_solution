import json
from collections import Counter

methods = Counter()
urls = Counter()
err = 0
total = 0

with open('access.log', encoding='utf-8') as f:
    for line in f:
        parts = line.split()
        if len(parts) >= 6:
            method = parts[3]
            url = parts[4]
            try:
                status = int(parts[5])
            except:
                status = 0
            methods[method] += 1
            urls[url] += 1
            total += 1
            if 400 <= status < 500:
                err += 1

stats = {
    'total': total,
    'methods': dict(methods),
    'err4xx': err,
    'top_url': urls.most_common(1)[0][0] if urls else None
}
print(json.dumps(stats, indent=2))
with open('stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, indent=2)
