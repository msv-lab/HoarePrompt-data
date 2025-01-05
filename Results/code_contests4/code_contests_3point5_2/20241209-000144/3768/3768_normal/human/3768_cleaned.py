stuff = raw_input().split()
xa = int(stuff[0])
ya = int(stuff[1])
xb = int(stuff[2])
yb = int(stuff[3])
xc = int(stuff[4])
yc = int(stuff[5])

def func_1(xa, ya, xb, yb, xc, yc):
    if ya < yb:
        if xa == xc and ya + yc == yb:
            print(yb)
            print(str('A' * xa + 'B' * xb + '\n') * ya + str('C' * xc + 'B' * xb + '\n') * yc)
            return True
    if ya == yb:
        if xa + xb == xc and ya + yc == xc:
            print(xc)
            print(str('A' * xa + 'B' * xb + '\n') * ya + str('C' * xc + '\n') * yc)
            return True
        if ya == yc and xa + xb + xc == yc:
            print(yc)
            print(str('A' * xa + 'B' * xb + 'C' * xc + '\n') * yc)
            return True
    if ya > yb:
        if xb == xc and yb + yc == ya:
            print(ya)
            print(str('A' * xa + 'B' * xb + '\n') * yb + str('A' * xa + 'C' * xc + '\n') * yc)
            return True
    if xa == xb:
        if xc == xa and ya + yb + yc == xa:
            print(xa)
            print(str('A' * xa + '\n') * ya + str('B' * xb + '\n') * yb + str('C' * xc + '\n') * yc)
            return True
    return False
if func_1(xa, ya, xb, yb, xc, yc):
    pass
elif func_1(ya, xa, xb, yb, xc, yc):
    pass
elif func_1(xa, ya, yb, xb, xc, yc):
    pass
elif func_1(xa, ya, xb, yb, yc, xc):
    pass
elif func_1(ya, xa, xb, yb, xc, yc):
    pass
elif func_1(xa, ya, yb, xb, xc, yc):
    pass
elif func_1(xa, ya, xb, yb, yc, xc):
    pass
elif func_1(ya, xa, yb, xb, yc, xc):
    pass
else:
    print(-1)