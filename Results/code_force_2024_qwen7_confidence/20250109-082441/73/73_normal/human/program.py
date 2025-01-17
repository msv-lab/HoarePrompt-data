t = int(input())
for _ in range(t):
    m, x = map(int, input().split())
    savings = 0
    count = 0
    happy = 0
    empty = []
    
    for i in range(m):
        c, h = map(int, input().split())
        empty.append((c, h))
    
    for c, h in empty:
        if count>0:
            savings+=x
        if c == 0:
            happy += h
            count+=1
        elif savings >= c:
            savings -= c
            happy += h
            count+=1
        else:
            savings+=x
    
    print(happy)