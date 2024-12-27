c, v0, v1, a, l = map(int, raw_input().split())

days = 0

while c > 0:
    c -= min(v0+days*a, v1)
    days += 1
    if c > 0:
        c += l

print(days)
