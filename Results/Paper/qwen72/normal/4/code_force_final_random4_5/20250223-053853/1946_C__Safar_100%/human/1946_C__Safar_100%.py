# import resource, sys
# sys.setrecursionlimit(10**7)
# resource.setrlimit(resource.RLIMIT_STACK, (10**7,-1))
# import sys
# sys.setrecursionlimit(999999999)
def solve(n,k,edges):
    g=[[] for _ in range(n+1)]
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    c=0
    def check(A):
        stack=[(1,1)]
        visited=set()
        d={1:1}
        r=0
        while True:
            x,p=stack[-1]
            if x not in visited:
                visited.add(x)
                d[x]=1
                for node in g[x]:
                    if node!=p:
                        stack.append((node,x))
            else:
                if(x==1):
                    break
                if(d[x]>=A):
                    r+=1
                else:
                    d[p]+=d[x]
                stack.pop()
                visited.remove(x)
                del d[x]
        # print(stack,d,r)
        if r>k or (d[1]>=A and r==k):
            return True
        return False
 
        # def dfs(x,y):
        #     c=1
        #     r=0
        #     for node in g[x]:
        #         if node==y:
        #             continue
        #         ans,rn=dfs(node,x)
        #         r+=rn
        #         if ans>=A:
        #             r+=1
        #         else:
        #             c+=ans
        #         # print(node,ans)
        #     return c,r
        
        # ans,r=dfs(1,1)
        # print(ans,r,x)
        # if r>k or (ans>=A and r==k):
        #     return True
        # return False
    # check(1)
    l=1
    r=(n//k)
    # print(l,r,n,k)
    while l<=r:
        mid=l+((r-l)//2)
        # print(mid,check(mid))
        if check(mid):
            l=mid+1
        else:
            r=mid-1
    # print(l,r)
    print(r)
 
q=[]
for i in range(int(input())):
    n,k=map(int,input().split(' '))
    edges=[]
    for _ in range(n-1):
        a,b=map(int,input().split(' '))
        edges.append((a,b))
    # if(i==325):
        # print(n,k,edges)
    solve(n,k,edges)
    # q.append((n,k,edges))
 
# print('ans:')
for n,k,edges in q:
    solve(n,k,edges)