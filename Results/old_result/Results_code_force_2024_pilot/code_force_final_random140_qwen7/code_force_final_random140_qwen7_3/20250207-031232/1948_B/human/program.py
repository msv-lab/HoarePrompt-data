def thing():
    k=int(input())
    a=input()
    a=list(map(int,a.split()))
    x=0
    y=0
    n=0
    c=[]
    for i in range(len(a)):
        if(a[i]>10 and i>0):
            x=int(a[i]%10)
            y=int(a[i]/10)
            if(y>=c[n-1]):
              if(y<=x): 
                 c.append(y)
                 c.append(x)
                 n=n+2
              else:
                 c.append(a[i])
                 n=n+1
            else:
               c.append(a[i])
               n=n+1
        elif(i==0 and a[i]>10):
            x=int(a[i]%10)
            y=int(a[i]/10)
            if(y<=x):
              c.append(y)
              c.append(x)
              n=n+2
            else:
               c.append(a[i])
               n=n+1
        else:
           c.append(a[i])
           n=n+1
    d=sorted(c)
    if(c==d):
       b.append(1)
    else:
       b.append(0)
m=int(input())
b=[]
for i in range(m):
   thing()
for i in range(m):
   if(b[i]==1):
      print("YES")
   else:
      print("NO")