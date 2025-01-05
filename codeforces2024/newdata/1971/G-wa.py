def solve():
    n = int(input())
    arr = list(map(int,input().split()))

    from collections import defaultdict

    d = defaultdict(lambda : [[],set({})])

    for i in range(n):
        curr = arr[i]
        d[curr>>2][0].append(i)
        d[curr>>2][1].add(arr[i])


    groups = d.keys()

    if(len(groups)==1):
        arr.sort()
    elif (len(groups))==n :
        pass
    else:
        for group in groups:
            temp_nums = d[group][1]
            temp_ind = d[group][0]
            for id,val in enumerate(temp_nums):
                arr[temp_ind[id]] = val
    
    print(" ".join(list(map(str,arr))))



        


t = int(input())

for _ in range(0,t):
    solve()
