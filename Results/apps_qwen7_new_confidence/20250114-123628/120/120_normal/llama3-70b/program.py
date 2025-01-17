import sys

n = int(input())

segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r, i + 1))

segments.sort()

ans_i, ans_j = -1, -1
min_r = sys.maxsize
for l, r, i in segments:
    if r < min_r:
        min_r = r
        ans_j = i
    elif r == min_r and l > segments[ans_j-1][0]:
        ans_i = i
        break

if ans_i != -1:
    print(ans_i, ans_j)
else:
    print(-1, -1)
