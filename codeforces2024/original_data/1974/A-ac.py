import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    if y%2==0:
        x-=(y//2)*7
        if x>0:
            print(y//2+math.ceil(x/15))
        else:
            print(y//2)
    else:
        x-=11+(y//2)*7
        if x>0:
            print(y//2+math.ceil(x/15)+1)
        else:
            print(y//2+1)
