def compress(lst):
    if not lst:
        return []
    res = []
    cur = lst[0]
    cnt = 1
    for x in lst[1:]:
        if x == cur:
            cnt += 1
        else:
            res.append((cur, cnt))
            cur = x
            cnt = 1
    res.append((cur, cnt))
    return res

def decompress(comp):
    res = []
    for val, cnt in comp:
        res.extend([val] * cnt)
    return res

a = [1, 1, 1, 2, 2, 5, 5, 5, 5, 3]
c = compress(a)
print(c)
print(decompress(c) == a)
