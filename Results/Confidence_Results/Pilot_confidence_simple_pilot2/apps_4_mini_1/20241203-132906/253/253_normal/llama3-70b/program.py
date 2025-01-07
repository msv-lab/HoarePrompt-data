n = int(input())
a = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]

max_score = 0
for i in range(n):
    for j in range(i, n):
        total = prefix_sum[j + 1] - prefix_sum[i]
        if j - i > 0:
            total -= min(a[i:j + 1])
        max_score = max(max_score, total)

print(max_score)
