
def solv(p1,p2,a1):

        
    ans1=0
    r=[]
    b=[]
    for i in a1:
        if(i[1]=='R'):
            r.append(i[0])
        elif(i[1]=='B'):
            b.append(i[0])
    ans1=2*(p2-p1)

    ans2=p2-p1
    if(len(r)):
        L=[r[0]-p1]
        R=[p2-r[-1]]
    
        for i in range(1,len(r)):
            L.append(r[i]-r[i-1] + L[-1])
        for i in range(len(r)-1,0,-1):
            R.append(r[i]-r[i-1] + R[-1])
        min1=min(L[-1],R[-1])
        for i in range(len(r)-1):
            min1=min(min1,L[i]+R[len(r)-i-2])
        ans2+=min1
    #print('ans2 due to r ',ans2,L,R)
    if(len(b)):
        L=[b[0]-p1]
        R=[p2-b[-1]]
    
        for i in range(1,len(b)):
            L.append(b[i]-b[i-1] + L[-1])
        for i in range(len(b)-1,0,-1):
            R.append(b[i]-b[i-1] + R[-1])
        min1=min(L[-1],R[-1])
        for i in range(len(b)-1):
            min1=min(min1,L[i]+R[len(b)-i-2])
        ans2+=min1
    #print('ans2 due to r ',ans2,L,R)
    #print('in solv ',ans1,ans2,p1,p2)
    return min(ans1,ans2)


n=int(raw_input())

a=[]
        
for i in range(n):
    x,y=raw_input().split()
    x=int(x)
    a.append([x,y])
first=-1
last=-1
ans=0
for i in range(n):
    if(a[i][1]=='P'):
        if(first==-1):
            first=i
        else:
            ans+=solv(a[last][0],a[i][0],a[last+1:i])
        last=i
    ans1=0
r=[]
b=[]
#print(ans)
if(first!=-1):
    for i in a[:first]:
        if(i[1]=='R'):
            r.append(i[0])
        elif(i[1]=='B'):
            b.append(i[0])
    for i in range(len(r)-1):
        ans+=r[i+1]-r[i]
    for i in range(len(b)-1):
        ans+=b[i+1]-b[i]
    if(len(r)):
        ans+=a[first][0]-r[-1]
    if(len(b)):
        ans+=a[first][0]-b[-1]
    r=[]
    b=[]
#    print(ans,r,b,first,a[:1])
    for i in a[last:]:
        if(i[1]=='R'):
            r.append(i[0])
        elif(i[1]=='B'):
            b.append(i[0])
    for i in range(len(r)-1):
        ans+=r[i+1]-r[i]
    for i in range(len(b)-1):
        ans+=b[i+1]-b[i]
    if(len(r)):
        ans+=r[0]-a[last][0]
    if(len(b)):
        ans+=b[0]-a[last][0]
else:
    r=[]
    b=[]
    
    for i in a:
        if(i[1]=='R'):
            r.append(i[0])
        elif(i[1]=='B'):
            b.append(i[0])
    for i in range(len(r)-1):
        ans+=r[i+1]-r[i]
    for i in range(len(b)-1):
        ans+=b[i+1]-b[i]
print(ans)




