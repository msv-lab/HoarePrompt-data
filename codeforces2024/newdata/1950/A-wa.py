n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a<b<c:
        print('STATR')
    if a<b and b>c:
        print('PEAK')
    else:
        print('NONE')
