for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    i = 0
    j = 0
    while i <= n - 1:
        if l[i] == i + 2 and l[i + 1] == i + 1:
            print(2)
            j = 1
            break
        i += 1
    if j == 0:
        print(3)