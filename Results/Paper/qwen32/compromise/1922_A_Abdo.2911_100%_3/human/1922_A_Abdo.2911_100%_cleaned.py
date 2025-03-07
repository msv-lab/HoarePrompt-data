def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()
        c = input().strip()
        possible = False
        for i in range(n):
            if a[i] == b[i]:
                if c[i] != a[i]:
                    possible = True
                    break
            elif c[i] == a[i] or c[i] == b[i]:
                continue
            else:
                possible = True
                break
        if possible:
            print('YES')
        else:
            print('NO')
func_1()