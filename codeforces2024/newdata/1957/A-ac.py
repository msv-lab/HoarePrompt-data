from collections  import Counter
import math
for _ in range(int(input())):
    n=int(input())
    edges=list(map(int,input().split()))

    count=Counter(edges)
    polygons=0

    for value in count.values():
        if value>2:
            polygons+=value//3
    print(polygons)