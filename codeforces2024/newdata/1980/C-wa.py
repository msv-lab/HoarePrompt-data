def counter(a, b):
    return a.count(b)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = int(input())
    d = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        if b[i] != a[i]:
            count += 1
    if count > m:
        print("No")
        continue
    
    valid = True
    for i in range(n):
        if b[i] != a[i] and b[i] not in d:
            print("No")
            valid = False
            break
    if not valid:
        continue
    
    for i in d:
        if counter(d, i) < counter(b, i):
            print("No")
            valid = False
            break
    if not valid:
        continue
    
    if d[m - 1] not in b:
        print("No")
        continue
    
    print("Yes")