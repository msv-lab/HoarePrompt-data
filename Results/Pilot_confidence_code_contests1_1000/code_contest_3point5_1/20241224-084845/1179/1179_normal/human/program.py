input=raw_input

n,m=map(int,input().split())
r=[]
for _ in range(m):
    a,b=map(int,input().split())
    r.append(b-a+1)
r.sort()
ans=r[0]
print(ans)
for i in range(n):
    print (i)%ans,
print("")