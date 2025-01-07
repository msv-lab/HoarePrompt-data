t = input().split(":")
h, m = int(t[0]), int(t[1])
if h == 23 and m == 59:
    print(1)
elif h * 100 + m == int(str(h * 100 + m)[::-1]):
    print(0)
else:
    while True:
        m += 1
        if m == 60:
            h += 1
            m = 0
        if h == 24:
            h = 0
        if h * 100 + m == int(str(h * 100 + m)[::-1]):
            print(m - int(t[1]))
            break
