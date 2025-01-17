def solution():
    n, m, k = list(map(int, input().split()))
    r_c = [list(map(lambda x: int(x)-1, input().split())) for _ in range(k)]
    idxs = list(range(k))
    idxs.sort(key=lambda x: (r_c[x][X], -r_c[x][Y]))
    result = [0]*k
    total = diff = 0
    prev, curr = 0, n
    x2 = y2 = -1
    j = -1
    for i in idxs:
        y, x = r_c[i]
        y = n-(y+1)
        if y >= curr:
            if y < y2:
                diff += (x-x2)*(y2-curr)
                x2, y2 = x, y
            continue
        if j != -1:
            diff += (x-x2)*(y2-curr)
            result[j] = diff
        j = i
        x2, y2, diff = x, curr, 0
        total += (x-prev)*curr
        prev, curr = x, y
    diff += (m-x2)*(y2-curr)
    result[j] = diff
    total += (m-prev)*curr
    return f'{total}\n{" ".join(map(str, result))}'
 
Y, X = list(range(2))
for _ in range(int(input())):
    print(solution())