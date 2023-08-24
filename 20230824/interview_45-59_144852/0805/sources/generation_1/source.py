n = int(input())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

alexey_l, alexey_r = segments[0]
total_length = 0

for i in range(101):
    if any(l <= i <= r for l, r in segments[1:]):
        continue

    if alexey_l <= i <= alexey_r:
        total_length += 1

print(total_length)