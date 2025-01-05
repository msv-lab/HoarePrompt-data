t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int,input().split())) 
    a.sort()
    a.append(a[-1] + 1)
    s = 0
    c = 0
    if a[0] != 0:
        print(0)
    else:
        for i in range(n -1):
            if a[i] != a[i+1]:
                if c == 0:
                    s += 1
                c = 0
            else:
                c += 1
            if s == 2:
                print(a[i])
                break
                
            
        else:
            print(a[-1])
            
                
            
