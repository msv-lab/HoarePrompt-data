x = int(input())
h, m = map(int, input().split())

counter = 0
while True:
    m -= x
    if m < 0:
        m += 60
        h -= 1
    if h < 0:
        h += 24
    if '7' in str(h) or '7' in str(m):
        break
    counter += 1

print(counter)