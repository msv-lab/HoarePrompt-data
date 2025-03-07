t=int(input())
for _ in range(t):
    p1,p2,p3=map(int,input().split())
    if (p1+p2+p3)%2!=0:
        print(-1)
        continue
    if p3>=p1+p2:
        print(p1+p2)
    else:
        x=0
        y=p3
        while y>=x:
            if p1-x<=p2-(y):
                print(p1-x+p3)
                break
            else:
                x+=1
                y-=1
        else:
            print(p3)