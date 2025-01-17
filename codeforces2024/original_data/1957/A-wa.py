from collections  import Counter
for _ in range(int(input())):
    n=int(input())
    edges=list(map(int,input().split()))

    count=Counter(edges)
    polygons=0
    for value in count.values():
        if value>2:
            polygons+=1
    print(polygons)