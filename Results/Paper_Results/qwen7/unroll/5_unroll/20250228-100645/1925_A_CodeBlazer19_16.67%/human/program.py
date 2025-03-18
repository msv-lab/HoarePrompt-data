t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=''
    for j in range(97,k+97):
        s+=chr(j)
    if k==1:
        print(n*s)
    else:
        print((2-(n==1))*s)