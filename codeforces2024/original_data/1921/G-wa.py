def calc(k, row, column, start, finish, f):
    addIt_lh = 0
    delIt_lh = 0
    addIt_rh = 0
    delIt_rh = 0
    addIt_rl = 0
    delIt_rl = 0
    addIt_ll = 0
    delIt_ll = 0

    for d in range(start, finish):
        if row-k+d >= 0 and f[row-k+d][column] == '#':#влево-вверх
            addIt_lh += 1
        if row-k+d >= 0 and column-1-d >= 0 and f[row-k+d][column-1-d] == '#':#влево-вверх
            delIt_lh += 1
        if row-k+d >= 0 and column+d < m and f[row-k+d][column+d] == '#':#вправо-вверх
            addIt_rh += 1
        if row-k+d >= 0 and column-1 >= 0 and f[row-k+d][column-1] == '#':#вправо-вверх
            delIt_rh += 1
        if row+d < n and column+k-d < m and f[row+d][column+k-d] == '#':#вправо-вниз
            addIt_rl += 1
        if row+d < n and column-1 >= 0 and f[row+d][column-1] == '#':#вправо-вниз
            delIt_rl += 1
        if row+d < n and f[row+d][column] == '#':#влево-вниз
            addIt_ll += 1
        if row+d < n and column-1-k+d >=0 and f[row+d][column-1-k+d] == '#':#влево-вниз
            delIt_ll += 1

    return addIt_lh, delIt_lh, addIt_rh, delIt_rh, addIt_rl, delIt_rl, addIt_ll, delIt_ll

for testInx in range(int(input())):
    n,m,k = map(int, input().split())

    f=[]
    for _ in range(n):
        f.append(input())

    res=0

    a=[]
    for row in range(n):
        a.append([])
        for column in range(m):
            a[row].append({'lh':0,'rh':0,'rl':0,'ll':0})
            if column==0:
                if row == 0:
                    #влево-вверх
                    if f[0][0] == '#':
                        a[row][column]['lh'] = 1
                    else:
                        a[row][column]['lh'] = 0
                    
                    addIt_rh = 0
                    addIt_rl = 0
                    addIt_ll = 0
                    for d in range(k+1):
                        if column+d < m and f[row][column+d] == '#':#вправо-вверх
                            addIt_rh += 1
                        for z in range(k+1-d): #вправо-вниз
                            if row+d < n and column+z < m and f[row+d][column+z] == '#':
                                addIt_rl += 1
                        if row+d < n and f[row+d][column] == '#':#влево-вниз
                            addIt_ll += 1
                    a[row][column]['rh'] = addIt_rh
                    a[row][column]['rl'] = addIt_rl
                    a[row][column]['ll'] = addIt_ll
                else:
                    #влево-вверх
                    addIt = 0
                    delIt = 0
                    if row-k-1 >= 0 and f[row-k-1][column] == '#':
                        delIt = 1
                    if f[row][0] == '#':
                        addIt = 1
                    a[row][column]['lh'] = a[row-1][column]['lh'] + addIt - delIt
                    
                    addIt_rh = 0
                    delIt_rh = 0
                    addIt_rl = 0
                    delIt_rl = 0
                    for d in range(k+1):
                        if row-1-k+d >= 0 and column+d < m and f[row-1-k+d][column+d] == '#':#вправо-вверх
                            delIt_rh += 1
                        if column+d < m and f[row][column+d] == '#':#вправо-вверх
                            addIt_rh += 1
                        if row+d < n and column+k-d < m and f[row+d][column+k-d] == '#':#вправо-вниз
                            addIt_rl += 1
                        if row-1 >= 0 and column+d < m and f[row-1][column+d] == '#':#вправо-вниз
                            delIt_rl += 1
                    a[row][column]['rh'] = a[row-1][column]['rh'] + addIt_rh - delIt_rh
                    a[row][column]['rl'] = a[row-1][column]['rl'] + addIt_rl - delIt_rl
                    #влево-вниз
                    addIt = 0
                    delIt = 0
                    if row+k < n and f[row+k][column] == '#':
                        addIt = 1
                    if row-1 >= 0 and f[row-1][column] == '#':
                        delIt = 1
                    a[row][column]['ll'] = a[row-1][column]['ll'] + addIt - delIt
            else:
                if not(k+1> n and k+1 > m):
                    addIt_lh, delIt_lh, addIt_rh, delIt_rh, addIt_rl, delIt_rl, addIt_ll, delIt_ll = calc(k, row, column, 0, k+1, f)

                    a[row][column]['lh'] = a[row][column-1]['lh'] + addIt_lh - delIt_lh
                    a[row][column]['rh'] = a[row][column-1]['rh'] + addIt_rh - delIt_rh
                    a[row][column]['rl'] = a[row][column-1]['rl'] + addIt_rl - delIt_rl
                    a[row][column]['ll'] = a[row][column-1]['ll'] + addIt_ll - delIt_ll

    #output
    for row in range(n):
        for column in range(m):
            if res < a[row][column]['lh']:
                res = a[row][column]['lh']
            if res < a[row][column]['rh']:
                res = a[row][column]['rh']
            if res < a[row][column]['rl']:
                res = a[row][column]['rl']
            if res < a[row][column]['ll']:
                res = a[row][column]['ll']
    print(res)
