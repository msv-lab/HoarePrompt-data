c, v0, v1, a, l = map(int, input().split())
days = 0
pages_read = 0
while pages_read < c:
    if days == 0:
        pages_to_read = min(v0, c - pages_read)
    else:
        pages_to_read = min(v0 + days * a, v1, c - pages_read)
    pages_read += pages_to_read - l
    days += 1
print(days)
