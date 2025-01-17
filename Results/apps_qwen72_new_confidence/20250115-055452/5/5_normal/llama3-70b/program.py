x = int(input())
hh, mm = map(int, input().split())

cur_min = hh * 60 + mm
while True:
    cur_min -= x
    if cur_min < 0:
        cur_min += 24 * 60
    h, m = divmod(cur_min, 60)
    if '7' in str(h) + str(m):
        break
print((hh * 60 + mm - cur_min) // x)
