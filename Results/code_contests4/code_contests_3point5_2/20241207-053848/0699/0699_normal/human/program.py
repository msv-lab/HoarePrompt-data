import sys
import math

def solve(n, x, a):
    x = float(x)
    mx = 0
    somme = reduce(lambda a,x: a + x, a, 0)
    for i in range(n):
        mx += math.ceil(a[i]/x)
    print("{} {}".format(int(somme/x), int(mx)))



if __name__ == "__main__":
    lines = [map(int, line.split()) for line in sys.stdin.readlines()]
    lines.pop(0)
    while lines:
        n = lines[0][0]
        x = lines[0][1]
        a = lines[1]
        solve (n, x, a)
        lines = lines[2::]