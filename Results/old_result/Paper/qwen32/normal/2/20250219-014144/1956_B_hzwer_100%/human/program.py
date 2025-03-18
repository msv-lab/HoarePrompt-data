import sys
 
input = sys.stdin.readline
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n + 1)
    for x in a:
        cnt[x] += 1
    ans = 0
    for x in cnt:
        ans += max(0, x - 1)
    print(ans)