t = int(input())
 
for tc in range(t):
 
    n = int(input())
    a = list(map(int, input().split()))
 
    maxsize = max(a)
 
    a.sort()
    mexsize = 1
    for sz in a:
        if sz == mexsize:
            mexsize = mexsize + 1
 
    if mexsize > maxsize:
        print("Alice" if mexsize % 2 == 0 else "Bob")
    else:
        print("Alice" if mexsize % 2 == 1 else "Bob")