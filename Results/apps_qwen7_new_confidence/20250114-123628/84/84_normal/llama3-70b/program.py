n = int(input())
a = list(map(int, input().split()))

for d in range(-1000, 1001):
    if d == 0:
        continue
    pos_count = sum(1 for x in a if (x / d) > 0)
    if pos_count >= (n + 1) // 2:
        print(d)
        break
else:
    print(0)
