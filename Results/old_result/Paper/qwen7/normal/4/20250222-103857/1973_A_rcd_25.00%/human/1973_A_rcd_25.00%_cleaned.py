t = int(input())
for _ in range(t):
    (p1, p2, p3) = map(int, input().split())
    if (p1 + p2 + p3) % 2 != 0:
        print(-1)
        continue
    if p3 >= p1 + p2:
        print(p1 + p2)
    else:
        (low, high) = (min(p3 - p1, p3 - p2), max(p3 - p1, p3 - p2))
        cur = low
        while high >= cur:
            if p1 - cur <= p2 - (p3 - cur):
                print(p1 - cur + p3)
                break
            else:
                cur += 1
        else:
            print(p3)