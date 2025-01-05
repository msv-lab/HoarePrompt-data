def find(a,b,c,d):
    print("?",a,b,c,d)
    return input()
    
for _ in range(int(input())):
    n,k = map(int,input().split())
    a = []
    for i in range(k):
        l = list(map(int,input().split()))
        a.append(l)
    if k==1 or n<3:
        print("YES")
    else:
        act = a[0][1:]
        find = -1
        for i in range(1,n):
            if a[1][i] == a[0][0]:
                find = i-1
        if find != 0:
            for i in range(n-1):
                if act[i] == a[1][find]:
                    act = act[:i+1] + [a[0][0]] + act[i+1:]
        else:
            find += 2
            for i in range(n-1):
                if act[i] == a[1][find]:
                    # print(act[:i],a[0][0],act[i:])
                    act = act[:i] + [a[0][0]] + act[i:]
                    break
            
                
        ok = "YES"
        # print(act,_+1)
        for i in range(1,k):
            x,y = 1,0
            while x<n and y<n:
                if a[i][x] == act[y]:
                    x += 1
                    y+=1
                elif a[i][0] == act[y]:
                    y+=1
                else:
                    ok = "NO"
                    break
        print(ok)