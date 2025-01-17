def is_unlucky(x, y, n):
    for a in range(61):
        for b in range(61):
            if x**a + y**b == n:
                return True
    return False

x, y, l, r = map(int, input().split())
max_golden_age = 0
start = l
while start <= r:
    if not is_unlucky(x, y, start):
        end = start
        while end <= r and not is_unlucky(x, y, end):
            end += 1
        max_golden_age = max(max_golden_age, end - start)
        start = end
    else:
        start += 1
print(max_golden_age)
