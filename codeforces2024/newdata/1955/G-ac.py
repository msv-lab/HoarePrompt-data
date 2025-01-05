from math import gcd

for _ in range(int(input())):
    n, m = tuple(map(int, input().split()))
    matr = []
    val = []
    for i in range(n):
        val.append([0] * m)
        matr.append(list(map(int, input().split())))
    
    val[0][0] = [matr[0][0]]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j != 0:
                val[i][j] = [gcd(val[i][j-1][0], matr[i][j])]
            elif i != 0 and j == 0:
                val[i][j] = [gcd(val[i-1][j][0], matr[i][j])]
            else:
                vals = []
                for v in val[i-1][j]:
                    vals.append(gcd(v, matr[i][j]))
                for v in val[i][j-1]:
                    vals.append(gcd(v, matr[i][j]))
                vals = sorted(list(set(vals)), reverse=True)
                val[i][j] = vals[:2]
                #val[i][j] = max(gcd(val[i-1][j], matr[i][j]), gcd(val[i][j-1], matr[i][j]))
    
    ans = val[-1][-1][0]
    '''
    val[-1][-1] = [matr[-1][-1]]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if i == n-1 and j == m-1:
                continue
            elif i == n-1 and j != m-1:
                val[i][j] = [gcd(val[i][j+1][0], matr[i][j])]
            elif i != n-1 and j == m-1:
                val[i][j] = [gcd(val[i+1][j][0], matr[i][j])]
            else:
                vals = []
                for v in val[i+1][j]:
                    vals.append(gcd(v, matr[i][j]))
                for v in val[i][j+1]:
                    vals.append(gcd(v, matr[i][j]))
                vals = sorted(list(set(vals)), reverse=True)
                val[i][j] = vals[:2]
                #val[i][j] = max(gcd(val[i+1][j], matr[i][j]), gcd(val[i][j+1], matr[i][j]))

    if val[0][0][0] > ans:
        ans = val[0][0][0]
    '''
    print(ans)


