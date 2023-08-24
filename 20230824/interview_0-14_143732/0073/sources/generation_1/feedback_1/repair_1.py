c, v0, v1, a, l = map(int, input().split())

days = 0
pages_read = 0
v = v0

while pages_read < c:
    pages_read += v
    v = min(v + a, v1)
    pages_read -= l
    days += 1

print(days)