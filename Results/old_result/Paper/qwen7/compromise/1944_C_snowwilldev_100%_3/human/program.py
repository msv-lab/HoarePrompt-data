from collections import defaultdict
def solve():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = defaultdict(int)
    for i in range(N): cnt[a[i]] += 1
    t = 0
    for i in range(N+1):
        if cnt[i] == 1: t += 1
        if t >= 2 or cnt[i] == 0: 
            return i
for tc in range(int(input())): print(solve())