def func_1():
    (n, x, y) = map(int, input().split())
    a = list(map(int, input().split()))
    a = [num - 1 for num in a]
    a.sort()
    present = set(a)
    ans = x - 2
    for i in range(x):
        t1 = (a[i] + 1) % n
        t2 = (a[i] + 2) % n
        if t1 not in present and t2 in present:
            ans += 1
    gaps = []
    for i in range(x):
        next_elem = a[(i + 1) % x] + (n if i == x - 1 else 0)
        gap = next_elem - a[i] - 1
        if gap > 0:
            gaps.append(gap)
    gaps.sort()
    for gap in gaps:
        pairs = gap // 2
        if y >= pairs:
            ans += gap
            y -= pairs
        else:
            ans += 2 * y
            break
    print(ans)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        func_1()