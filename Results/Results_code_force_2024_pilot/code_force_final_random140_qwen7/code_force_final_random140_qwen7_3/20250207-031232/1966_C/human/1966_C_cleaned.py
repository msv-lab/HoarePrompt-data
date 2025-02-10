for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set()
    for i in range(n):
        s.add(arr[i])
    s = list(s)
    ans = 1
    s = [0] + s
    n = len(s)
    if n == 2:
        print('Alice')
    else:
        for i in range(1, n - 1):
            if s[i] - s[i - 1] > 1:
                break
            else:
                ans = 1 - ans
        if ans:
            print('Alice')
        else:
            print('Bob')