n = int(input())
a = list(map(int, input().split()))

pos1 = a.index(1)
posn = a.index(n)

max_dist = max(abs(pos1 - posn) - 1, n - 2)
min_dist = min(abs(pos1 - posn) - 1, n - 2)

print(max(max_dist, n - 1 - min_dist))
