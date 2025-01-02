import sys
sys.setrecursionlimit(10 ** 6)
# pow(3,2,5)==4

n,x,y=map(int,raw_input().split())
inp2=map(int,raw_input().split())
for i in range(n):
    flag=True
    val=inp2[i]
    for bef in range(1,x+1):
        indis=i-bef
        if indis<0:
            break
        if indis>=n:
            break
        if val>inp2[indis]:
            flag=False
            break
    for aft in range(1,y+1):
        indis=i+aft
        if indis<0:
            break
        if indis>=n:
            break
        if val>inp2[indis]:
            flag=False
            break
    if flag:
        print(i+1)
        break
