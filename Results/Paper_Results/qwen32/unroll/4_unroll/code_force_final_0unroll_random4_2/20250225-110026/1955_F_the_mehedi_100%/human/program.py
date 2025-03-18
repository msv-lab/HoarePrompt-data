import math
for _ in range(int(input())):
    a = list(map(int,input().split()))
    cnt = 0
    if a[0]%2==a[1]%2==a[2]%2==1 :
        cnt+=1
    for x in a:
        cnt+=math.floor(x/2)
    print(cnt)