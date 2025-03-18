for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set()
    for i in range(n):
        s.add(arr[i])
    s = list(s)
    s.sort()
    s = [0] + s
    ans = 1
    n = len(s)
    if n == 2:
        print('Alice')
    else:
        for i in range(1, n - 1):
            if s[i] - s[i - 1] > 1:
                break
            else:
                ans ^= 1
        if ans:
            print('Alice')
        else:
            print('Bob')