from collections import defaultdict
import math

for p in range(int(input())):
    n,=map(int,input().split())
    c=list(map(int,input().split()))
    tree=defaultdict(lambda:[])
    d=defaultdict(int)
    for i in range(n-1):
        l,r=map(int,input().split())
        tree[l].append(r);tree[r].append(l)
        d[l]+=1;d[r]+=1
        if d[l]==1:
            root=l
        if d[r]==1:
            root=r
    # print(tree)
#     print(d)
#     print(root)

    def function(root):
        for child in tree[root]:
            if root in tree[child]:
                tree[child].remove(root)
            function(child)
    function(root)
    # print(tree)
    count=[0]
    dic=[(0) for i in range(n)]
    def backtrack(root,count):
        dic[root-1]=defaultdict(lambda:(0,0))
        for child in tree[root]:
            d=backtrack(child,count)
            for key in d.keys():
                dic[root-1][key]=(dic[root-1][key][0]+d[key][0],dic[root-1][key][1]+d[key][1])
#         print(dic[root-1])
        count[0]+=dic[root-1][c[root-1]][0]+dic[root-1][c[root-1]][1]
        dic[root-1][c[root-1]]=(1,0)
#         print(count[0])
        for key in dic[root-1].keys():
            if dic[root-1][key][0]>1:
                count[0]+=(dic[root-1][key][0]*(dic[root-1][key][0]-1))//2
                dic[root-1][key]=(0,dic[root-1][key][0]+dic[root-1][key][1])
#         print(dic[root-1],count)
        return dic[root-1]

    d=(backtrack(root,count))
    for key in d.keys():
        count[0]+=(dic[root-1][key][0]*(dic[root-1][key][0]-1))//2
    print(count[0])
