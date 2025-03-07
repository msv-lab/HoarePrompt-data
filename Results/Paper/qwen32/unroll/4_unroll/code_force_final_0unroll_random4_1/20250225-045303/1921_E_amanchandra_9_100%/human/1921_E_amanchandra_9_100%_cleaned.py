t = int(input())
for _ in range(t):
    (r, w, a, b, c, d) = list(map(int, input().split()))
    if a > c:
        print('Draw')
    else:
        x = abs(a - c) // 2
        if abs(a - c) % 2:
            l = max(1, d - x)
            r = min(w, d + x)
            print(*(['Draw'], ['Alice'])[abs(l - b) <= x + 1 and abs(r - b) <= x + 1])
        else:
            l = max(1, b - x)
            r = min(w, b + x)
            print(*(['Draw'], ['Bob'])[abs(l - d) <= x and abs(r - d) <= x])