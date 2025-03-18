for i in range(int(input())):
    h,w,xa,ya,xb,yb= map(int,input().split())
    
    if xa>xb: print('Draw')
    else:
        x=abs(xa-xb)//2
        if abs(xa-xb)%2:
            l=max(1,yb-x)
            r=min(w,yb+x)
            # print('###',l,r,x,abs(xa-xb),abs(l-ya),abs(r-ya))
            print(*(['Draw'],['Alice'])[abs(l-ya)<=x+1 and abs(r-ya)<=x+1])
        else:
            l=max(1,ya-x)
            r=min(w,yb+x)
            # print('@@@',l,r,x,abs(xa-xb),abs(l-yb),abs(r-yb))
            print(*(['Draw'],['Bob'])[abs(l-yb)<=x and abs(r-yb)<=x])