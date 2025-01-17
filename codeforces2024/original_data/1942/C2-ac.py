t = int(input())

for _ in range(t):
    n, x, y = list(map(int, input().split()))
    a = list(map(int,input().split()))

    a = [num - 1 for num in a]  

    ans = x - 2
    st = set(a)
    a.sort()

    for i in range(x):
        t1 = (a[i] + 1) % n
        t2 = (a[i] + 2) % n
        if t1 not in st and t2 in st:
            ans += 1

    odd = []
    even = []

    for i in range(x):
        next_elem = a[0] + n if i == x - 1 else a[i + 1]
        gap = next_elem - a[i] - 1
        if gap > 1 and gap % 2 == 1:
            odd.append(gap)
        elif gap > 0 and gap % 2 == 0:
            even.append(gap)

    odd.sort()
    even.sort()

    for gap in odd:
        if y < gap // 2:
            ans += 2 * y
            y = 0
            break
        ans += gap
        y -= gap // 2

    for gap in even:
        if y < gap // 2:
            ans += 2 * y
            y = 0
            break
        ans += gap
        y -= gap // 2

    print(ans)
