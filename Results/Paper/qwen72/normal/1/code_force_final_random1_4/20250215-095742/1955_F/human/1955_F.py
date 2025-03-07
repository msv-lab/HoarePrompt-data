for _ in range(int(input())):
    p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
    print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)