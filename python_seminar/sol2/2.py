nums = []
with open('numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                nums.append(int(line))
            except ValueError:
                pass

if nums:
    mn = min(nums)
    mx = max(nums)
    avg = sum(nums) / len(nums)
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write(f'{mn}\n{mx}\n{avg}\n')
