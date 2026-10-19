total = 0
count = 0
mn = None
mx = None

with open('nums.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            n = int(line)
        except ValueError:
            continue
        total += n
        count += 1
        if mn is None or n < mn:
            mn = n
        if mx is None or n > mx:
            mx = n

if count:
    print(total, mn, mx, count, total / count)
