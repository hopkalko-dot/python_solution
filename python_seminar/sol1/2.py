best = None
best_cnt = -1

while True:
    s = input()
    if s.upper() == 'STOP':
        break
    cnt = len(set(s.lower()))
    if cnt > best_cnt:
        best_cnt = cnt
        best = s

print(best, best_cnt)
