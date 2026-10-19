def nearest(points, x0, y0):
    if not points:
        return None, None
    best = points[0]
    best_d = (best[0] - x0) ** 2 + (best[1] - y0) ** 2
    for p in points[1:]:
        d = (p[0] - x0) ** 2 + (p[1] - y0) ** 2
        if d < best_d:
            best_d = d
            best = p
    return best, best_d ** 0.5

print(nearest([(1, 1), (3, 4), (0, 0)], 0, 0))
