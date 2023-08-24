def trip_duration(O, D, n, lines):
    o2i = {O: 0}
    i2o = [O]
    d2i = {D: n+1}
    lines = [[O, D, 0, 0]] + lines + [[D, O, 0, 0]]
    for line in lines:
        if line[0] not in o2i:
            o2i[line[0]] = len(o2i)
            i2o.append(line[0])
        if line[1] not in d2i:
            d2i[line[1]] = len(d2i)
    
    start = o2i[O]
    end = d2i[D]
    
    longest_precalculation = 120
    precalculation = [[-1 for i in range(len(d2i))] for j in range(len(o2i))]
    
    for i1 in range(len(precalculation)):
        for i2 in range(len(precalculation[i1])):
            point1 = i2o[i1]
            point2 = i2o[i2]
            
            if point1 == point2:
                precalculation[i1][i2] = 0
                continue
            if point1 == O and point2 == D:
                precalculation[i1][i2] = 0
                continue
            
            backup = []
            ok = False
            
            for j in range(1, len(lines)):
                if not ok and lines[j][0] == point1:
                    ok = True
                    backup = []
                if not ok:
                    continue
                if lines[j][1] == point2:
                    precalculation[i1][i2] = lines[j][2] + lines[j][3]
                    break
                backup.append(lines[j][3])
            
            if precalculation[i1][i2] == -1:
                precalculation[i1][i2] = longest_precalculation
            
            for j in range(len(backup)):
                precalculation[i1][i2] = min(precalculation[i1][i2], longest_precalculation + backup[j])
    
    def f(i, j, add):
        return precalculation[i][j] + add
    
    before = [[(-1, -1, -1) for j in range(len(d2i))] for i in range(len(o2i))]
    before[start][start] = (0, start, 0)
    
    q = []
    heapq.heappush(q, (0, (start, start, 0)))
    
    done = set()
    
    while len(q) > 0:
        (a, b) = heapq.heappop(q)
        i = b[0]
        j = b[1]
        add = b[2]
        
        if before[i][j] != (a, add, 0):
            continue
        if j == end:
            break
        
        done.add((i, j))
        for k in range(len(precalculation[j])):
            if (j, k) in done:
                continue
            if precalculation[j][k] == longest_precalculation:
                continue
                
            a = f(i, j, add)
            b1 = before[i][j]
            if b1[2] + a - b[2] <= 120:
                c = (a, b[1], b1[2] + a - b[2])
            else:
                c = (a, b[1], 120)
            
            if before[j][k] == (-1, -1, -1):
                before[j][k] = (c[0], c[1], c[2])
                heapq.heappush(q, (c[0], (j, k, 0)))
            elif d2i[c[1]] == d2i[before[j][k][1]] and c[2] < before[j][k][2]:
                before[j][k] = (c[0], c[1], c[2])
                heapq.heappush(q, (c[0], (j, k, 0)))
    
    d = {}
    for i in range(len(i2o)):
        d[i2o[i]] = i
    
    x = []
    i = before[end][end]
    
    while True:
        if i[1] == start:
            break
        x.insert(0, i[0])
        i = before[i[1]][i[1]]
    
    return sum(x) / 60.0


origin, destination = input().split()
n = int(input())
lines = []
for i in range(n):
    lines.append(list(map(int, input().split())))

result = trip_duration(origin, destination, n, lines)
print(format(result, ".6f"))