for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if a*2 < b:
        print(n * a)
    elif n % 2 == 0:
        print(b * (n//2))
    else:
        print((b * (n//2))+a) 