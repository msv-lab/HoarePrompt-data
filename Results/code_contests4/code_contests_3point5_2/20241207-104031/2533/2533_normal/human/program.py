from fractions import Fraction
import sys

def InputIterator():
    for line in sys.stdin:
        for value in line.split(): yield value

inp = InputIterator()

n = int(next(inp))
x1 = int(next(inp))
y1 = int(next(inp))
x2 = int(next(inp))
y2 = int(next(inp))

t1, t2 = Fraction(0, 1), None

for i in xrange(n):
    rx = int(next(inp))
    ry = int(next(inp))
    vx = int(next(inp))
    vy = int(next(inp))

    if vx != 0:
        if vx > 0:
            t1 = max(t1, Fraction(x1-rx, vx))

            if t2 is None:
                t2 = Fraction(x2-rx, vx)
            else:
                t2 = min(t2, Fraction(x2-rx, vx))
        else:
            if t2 is None:
                t2 = Fraction(x1-rx, vx)
            else:
                t2 = min(t2, Fraction(x1-rx, vx))

            t1 = max(t1, Fraction(x2-rx, vx))
    else:
        if rx <= x1 or rx >= x2:
            print(-1)
            sys.exit(0)

    if vy != 0:
        if vy > 0:
            t1 = max(t1, Fraction(y1-ry, vy))

            if t2 is None:
                t2 = Fraction(y2-ry, vy)
            else:
                t2 = min(t2, Fraction(y2-ry, vy))
        else:
            if t2 is None:
                t2 = Fraction(y1-ry, vy)
            else:
                t2 = min(t2, Fraction(y1-ry, vy))

            t1 = max(t1, Fraction(y2-ry, vy))
    else:
        if ry <= y1 or ry >= y2:
            print(-1)
            sys.exit(0)

if t2 is None:
    print(format(t1.numerator/t1.denominator, '.20f'))
else:
    if t2 <= t1:
        print(-1)
    else:
        print(format(t1.numerator/t1.denominator, '.20f'))
