def spiral(n, m, reverse=False):
    mat = [[0] * m for _ in range(n)]
    total = n * m
    nums = list(range(total, 0, -1)) if reverse else list(range(1, total + 1))
    i = 0
    top, bot, left, right = 0, n - 1, 0, m - 1
    while top <= bot and left <= right:
        for c in range(left, right + 1):
            mat[top][c] = nums[i]
            i += 1
        top += 1
        for r in range(top, bot + 1):
            mat[r][right] = nums[i]
            i += 1
        right -= 1
        if top <= bot:
            for c in range(right, left - 1, -1):
                mat[bot][c] = nums[i]
                i += 1
            bot -= 1
        if left <= right:
            for r in range(bot, top - 1, -1):
                mat[r][left] = nums[i]
                i += 1
            left += 1
    return mat

print(spiral(3, 3))
print(spiral(3, 5))
print(spiral(4, 2))
