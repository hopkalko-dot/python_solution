def moving_avg(data, k):
    if k <= 0 or k > len(data):
        raise ValueError
    s = sum(data[:k])
    res = [s / k]
    for i in range(k, len(data)):
        s += data[i] - data[i - k]
        res.append(s / k)
    return res

print(moving_avg([2, 4, 6, 8, 10], 3))
