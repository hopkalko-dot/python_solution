def analyze(path):
    total = 0
    cnt = 0
    mn = None
    mx = None
    passed = 0
    best = ''
    best_s = -1
    with open(path, encoding='utf-8') as f:
        for line in f:
            if ';' not in line:
                continue
            try:
                name, sc = line.strip().rsplit(';', 1)
                sc = int(sc)
            except:
                continue
            total += sc
            cnt += 1
            if mn is None or sc < mn:
                mn = sc
            if sc > best_s:
                best_s = sc
                best = name
            if sc >= 60:
                passed += 1
    if cnt:
        print(total / cnt, mx, mn, passed, best)

analyze('grades.txt')
