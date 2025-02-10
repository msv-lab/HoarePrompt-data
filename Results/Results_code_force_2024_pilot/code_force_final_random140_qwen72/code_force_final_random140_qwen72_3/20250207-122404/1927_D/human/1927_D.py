R=lambda:map(int,input().split())
t,=R()
while t:
 t-=1;R();a=[0];p=i=j=0;
 for x in R():j=(j,i)[x!=p];a+=j,;p=x;i+=1
 q,=R()
 while q:q-=1;l,r=R();print(*((a[r],r),[-1]*2)[a[r]<l])