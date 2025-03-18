for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    same = 1
    num = ar[0]
    minn = inf
    i = 1
    while i < len(ar):
        if ar[i] == num:
            same += 1
        else:
            i += 1
            num = ar[i]
            minn = min(minn, same)
            same = 1
        i += 1
    minn = min(minn, same)
    if minn == inf or minn == len(ar):
        print(-1)
    else:
        print(minn)