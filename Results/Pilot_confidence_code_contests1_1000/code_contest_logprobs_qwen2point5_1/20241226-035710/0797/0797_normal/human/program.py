import sys
import math
import bisect

n,q = list(map(int, sys.stdin.readline().strip().split(' ')))

notifications = []
unread = [0 for i in range(n+1)]
last_unread = 0
ans = 0
for q0 in range(q):
    i,x = list(map(int, sys.stdin.readline().strip().split(' ')))
    if i == 1:
        unread[x] += 1
        ans += 1
        notifications.append(x)
    elif i == 2:
        ans -= unread[x]
        unread[x] = 0
    else:
        for j in range(last_unread,x):
            unread[notifications[j]] -= 1
            ans -= 1
        last_unread = x
    print(ans)