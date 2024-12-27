from __future__ import print_function

def __main__():
    inp = raw_input().split(' ')
    N = int(inp[0])
    D = int(inp[1])
    S = int(inp[2])

    a = []
    au = []
    for i in range(N):
        inp = raw_input().split(' ')
        a.append([int(inp[0]), int(inp[1]), int(inp[2]), False])
        if int(inp[2]) >= D:
            au.append((float(inp[1]), float(inp[0]), i))
            
    def __less(a, b):
        if a[0] == 0:
            return -1
        elif b[0] == 0:
            return 1
        else:
            return -cmp(a[1]/a[0], b[1]/b[0])
        
    au.sort(__less)
    #print(au)
    m = 0
    s = S
    res = 0
    for i in au:
        if a[i[2]][1] <= s:
            s -= a[i[2]][1]
            a[i[2]][3] = True
            m += a[i[2]][0]
            res += 1

    b = [i[0] for i in a if not i[3]]
    b.sort(reverse=True)
    #print(b)

    for i in b:
        if m <= 0:
            break
        else:
            m += i - 1
            res += 1
    if res == 0:
        print('0 0')
    else:
        print(res, S - s)

__main__()
