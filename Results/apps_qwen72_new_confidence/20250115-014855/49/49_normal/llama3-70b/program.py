n, m, k = map(int, input().split())
count = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        num = i * j
        if num not in count:
            count[num] = 0
        count[num] += 1
sorted_count = sorted(count.items(), reverse=True)
ans = 0
for num, cnt in sorted_count:
    k -= cnt
    if k <= 0:
        ans = num
        break
print(ans)
