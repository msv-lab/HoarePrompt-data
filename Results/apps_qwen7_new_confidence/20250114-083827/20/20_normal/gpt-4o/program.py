T = int(input())

for _ in range(T):
    n = int(input())
    records = []
    for _ in range(n):
        p, c = map(int, input().split())
        records.append((p, c))
    
    valid = True
    
    for i in range(n):
        p, c = records[i]
        if c > p:
            valid = False
            break
        if i > 0:
            p_prev, c_prev = records[i-1]
            if p < p_prev or c < c_prev or (p - p_prev) < (c - c_prev):
                valid = False
                break
    
    if valid:
        print("YES")
    else:
        print("NO")
