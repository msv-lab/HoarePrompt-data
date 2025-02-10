for _ in range(int(input())):
    k, x, a = map(int, input().split())
    s = 1
    for i in range(x):
        s += s//(k-1) + 1
    print("YES" if a>=s else "NO")