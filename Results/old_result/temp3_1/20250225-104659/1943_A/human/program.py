def func():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        cntl = [0 for _ in range(n + 1)]
        for i in a:
            cntl[i] += 1
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    if cntl[j] == 0:
                        print(j)
                        break
                    else:
                        c -= 1
                        if not c:
                            print(j)
                            break

