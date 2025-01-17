# LUOGU_RID: 150732124
def r(x):
    x=int(x)
    if f==0:return b[x]
    for i in range(f-1,-1,-1):
        if a[2*i]>=x:continue
        if a[2*i+1]<x:
            x%=a[2*i+1]
            if x==0:return b[a[2*i+1]]
            if a[2*i]>=x:continue
        return b[x]
for _ in range(int(input())):
    a=[0,0];b={};c,d=map(int,input().split());f=0
    for i in range(c):
        d,e=map(int,input().split())
        if d&1:a[-1]+=1;b[a[-1]]=e
        else:
            if a[-1]-a[-2]:a.append(a[-1]);a[-1]*=(e+1);a.append(a[-1]);f+=1
            else:a[-2]*=(e+1);a[-1]=a[-2]
    print(str(list(map(r,input().split())))[1:-1].replace(',',''))