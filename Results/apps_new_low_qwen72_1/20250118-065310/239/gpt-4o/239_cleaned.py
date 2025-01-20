def func_1(n, m, k, a):
    max_cost = 0
    current_sum = 0
    min_prefix = 0
    for i in range(n):
        current_sum += a[i]
        if i + 1 >= m:
            current_cost = current_sum - k * math.ceil((i + 1) / m)
            max_cost = max(max_cost, current_cost - min_prefix)
            min_prefix = min(min_prefix, current_cost)
    return max_cost
input = sys.stdin.read
data = input().split()
(n, m, k) = (int(data[0]), int(data[1]), int(data[2]))
a = list(map(int, data[3:]))
print(func_1(n, m, k, a))