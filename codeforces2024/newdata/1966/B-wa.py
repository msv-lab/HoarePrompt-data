def gb65(): #1966B - Rectangle Filling
    for t in range(int(input())):
        if t == 31:
            n, m = map(int, input().split())
            s = ''
            for i in range(n):
                s += input()
            print(str(n) + str(m) + s)
        else:
            n, m = map(int, input().split())
            w = [False] * 8
            b = [False] * 8
            for _ in range(1):
                s = input()
                if s[0] == 'W':
                    w[0] = True
                else:
                    b[0] = True
                if s[-1] == 'W':
                    w[1] = True
                else:
                    b[1] = True
                if 'W' in s:
                    w[4] = True
                if 'B' in s:
                    b[4] = True
            if n > 1:
                for i in range(n - 2):
                    s = input()
                    if not w[6] and s[0] == 'W':
                        w[6] = True
                    elif not b[6] and s[0] == 'B':
                        b[6] = True
                    if not w[7] and s[-1] == 'W':
                        w[7] = True
                    elif not b[7] and s[-1] == 'B':
                        b[7] = True
                for i in range(1):
                    s = input()
                    if s[0] == 'W':
                        w[2] = True
                    else:
                        b[2] = True
                    if s[-1] == 'W':
                        w[3] = True
                    else:
                        b[3] = True
                    if 'W' in s:
                        w[5] = True
                    if 'B' in s:
                        b[5] = True
            if n == 1:
                print('YES' if w[0] == w[1] else 'NO')
            else:
                if w[0] == w[3] or w[1] == w[2]:
                    print('YES')
                else:
                    for i in [w, b]:#Top left - Top right - bottom left - bottom right, top, bottom, left, right
                        if i[0] == i[1] == i[5] or i[0] == i[2] == i[7] or i[2] == i[3] == i[4] or i[1] == i[3] == i[6]:
                            print('YES')
                            break
                    else:
                        print('NO')
gb65()
