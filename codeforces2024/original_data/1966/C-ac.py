t = int(input())
for _ in range(t):
    n = int(input())
    a = list(set(list(map(int, input().split()))))
    a.sort()
    x = 0
    if a[0] == 1:
        for i in range(1,len(a)):
            if a[i] == a[i-1]+1 and a[i] == i+1:
                x+=1
        x += 1
    tt = len(a) - x
    # print("SASd", a)
    # print("T",_+1,x)
    if x%2==0:
        if tt == 0:
            print("Bob")
        else:
            print("Alice")
    else:
        if tt == 0:
            print("Alice")
        else:
            print("Bob")