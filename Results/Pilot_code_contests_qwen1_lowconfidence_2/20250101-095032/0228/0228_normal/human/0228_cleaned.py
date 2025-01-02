vp = int(raw_input())
vd = int(raw_input())
t_read = int(raw_input())
f = int(raw_input())
c = int(raw_input())
pl = 0
dl = 0
t = 1
count = 0
while pl + vp <= c:
    pl += vp
    if t > t_read:
        dl += vd
        if dl >= pl and pl + vp <= c:
            count += 1
            dl = pl
            pl += (2 * (dl / vd) + f) * vp
    t += 1
print(count)