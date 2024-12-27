x = int(raw_input())
a,b = map(int,raw_input().split())
if "7" in str(a) or "7" in str(b):
    print(0)
else:
    total = a*60+b
    ans = 0 
    for i in range(total,-1,-1):
        l,m = i//60,i%60
        if "7" in str(l) or "7" in str(m):
            ans = i
            break
    if not ans:
        total = 23*60  + 59
        for i in range(total,-1,-1):
            l,m = i//60,i%60
            if "7" in str(l) or "7" in str(m):
                ans = i
                break
    j  = 0
    print((total-ans)//x + j)
