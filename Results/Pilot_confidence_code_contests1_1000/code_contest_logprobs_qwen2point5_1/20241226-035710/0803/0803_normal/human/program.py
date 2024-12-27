from sys import stdin


def pow1(x, base):
    sq = 0
    while (base > 0):

        if base % 2:
            base -= 1

        base //= 2
        sq += 1

    return sq


x, y = map(int, stdin.readline().split())
ans1, ans2 = pow1(x, y), pow1(y, x)

if ans1 > ans2:
    print('>')
elif ans1 < ans2:
    print('<')
else:
    print('=')
