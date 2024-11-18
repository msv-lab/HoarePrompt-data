def func_1(n, k):
    min_sum = k * (k + 1) // 2
    if min_sum > n:
        return -1
    d = n // min_sum
    remainder = n - d * min_sum
    sequence = [d * (i + 1) for i in range(k)]
    for i in range(k - 1, -1, -1):
        if remainder == 0:
            break
        sequence[i] += 1
        remainder -= 1
    return sequence
(n, k) = map(int, input().split())
result = func_1(n, k)
if result == -1:
    print(-1)
else:
    print(' '.join(map(str, result)))