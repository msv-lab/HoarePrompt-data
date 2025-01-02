from sys import stdin, gettrace

if gettrace():
    def inputi():
        return input()
else:
    def input():
        return next(stdin)[:-1]


    def inputi():
        return stdin.buffer.readline()


def solve():
    n, m = map(int, input().split())
    aa = [int(a) for a in input().split()]
    bb = [int(a) for a in input().split()]
    if sum(aa) < m:
        print(-1)
        return
    lp = [0, 0] + [aa[i] for i in range(n) if bb[i] == 1]
    hp = [0] + [aa[i] for i in range(n) if bb[i] == 2]
    lp.sort()
    hp.sort()
    rm = m
    res = 0
    while rm > 0:
        if lp[-1] >= rm:
            res += 1
            break
        if hp[-1] > lp[-1] + lp[-2]:
            res += 2
            rm -= hp.pop()
        else:
            res += 1
            rm -= lp.pop()
    print(res)


def main():
    t = int(input())
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
