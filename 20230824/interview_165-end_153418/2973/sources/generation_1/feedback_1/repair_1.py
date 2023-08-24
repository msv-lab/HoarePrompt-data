n, t = map(int, input().split())

distance = 0
total_time = 0
for _ in range(n):
    d, s = map(int, input().split())
    distance += d
    total_time += d / s

c = (distance - t * total_time) / t

print("{:.9f}".format(c))