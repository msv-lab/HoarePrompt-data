for i in range(int(input())):
    A, B, C = map(int,input().split())
    if (B *2) < C:
        print(A*B)
    else:
        if A % 2 == 0:
            print(int((A * C)/2))
        else:
            X = A // 2
            print(X)
            print((X * C) + B)