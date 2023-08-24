n, t = map(int, input().split())

distance = 0
speed = 0
for _ in range(n):
    d, s = map(int, input().split())
    distance += d
    speed += s

c = (distance - t * speed) / t

print(c)