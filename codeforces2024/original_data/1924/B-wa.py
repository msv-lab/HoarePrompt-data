import bisect

def solution():
    n, m, q = map(int, input().split())
    xs = list(map(int, input().split()))
    vs = list(map(int, input().split()))
    a = sorted([(x, v) for x, v in zip(xs, vs)])
    for _ in range(q):
        row = tuple(map(int, input().split()))
        if row[0] == 1:
            _, x, v = row
            bisect.insort(a, (x, v))
        else:
            _, l, r = row
            # print(l, r, a)
            result = 0
            i = bisect.bisect_left(a, (l, 0))
            while i < len(a):
                x1, v1 = a[i - 1]
                x2, v2 = a[i]
                if r <= x1:
                    break
                d1 = x2 - max(x1 + 1, l)
                d2 = x2 - min(x2, r)
                inc = v1 * (d2 + d1) * (d1 - d2 + 1) // 2
                # print(f'{x1}..{x2} x {v1}, {d1}..{d2}, {inc}')
                result += inc
                i += 1
            print(result)

solution()