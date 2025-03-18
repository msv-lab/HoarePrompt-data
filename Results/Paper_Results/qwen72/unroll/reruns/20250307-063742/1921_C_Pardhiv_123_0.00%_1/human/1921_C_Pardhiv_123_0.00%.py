t=int(input(""))
while(t>0):
    n,f,a,b=map(int,input("").split(" "))
    ls=list(map(int,input("").split(" ")))
    for i in range(1,len(ls)):
        f=f-min(a*(ls[i]-ls[i-1]),b)
    if(f>0):
        print("YES")
    else:
        print("NO")
    t-=1