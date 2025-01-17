n = int(input())
a = list(map(int, input().split()))
total = sum(a)
half = total // 2
curr = 0
for i in range(n):
    curr += a[i]
    if curr >= half:
        print(i + 1)
        break
