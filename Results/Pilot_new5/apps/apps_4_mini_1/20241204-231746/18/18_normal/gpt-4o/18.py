n, k, t = map(int, input().split())

# Determine the number of spectators standing at time t
if t <= k:
    print(t)
elif t <= n:
    print(k)
else:
    print(n + k - t)
