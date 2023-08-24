c, v0, v1, a, l = map(int, input().split())

days = 1
pages_read = v0
while pages_read < c:
    v = min(pages_read + a, v1)
    pages_read += v - l
    days += 1

print(days)