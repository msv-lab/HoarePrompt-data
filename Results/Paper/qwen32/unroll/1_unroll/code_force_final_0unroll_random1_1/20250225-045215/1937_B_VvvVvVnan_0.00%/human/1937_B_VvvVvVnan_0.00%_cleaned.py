"""
t=int(input())
fin=['NO']*t
for i in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    l=len(a)-1
    r=0
    flag=True
    while r<=l and flag:
        if a[r]!=0:
            a[r+1]=a[r+1]-2*a[r]
            a[r+2]=a[r+2]-a[r]
            a[r]=0
            if a[r+1]<0 or a[r+2]<0:
                flag=False
        if a[l]!=0:
            a[l-1]=a[l-1]-2*a[l]
            a[l-2]=a[l-2]-a[l]
            a[l]=0
            if a[l-1]<0 or a[l-2]<0:
                flag = False
        r=r+1
        l=l-1
    if flag==True:
        fin[i]='YES'
for i in range(t):
    print(fin[i])
"""

def func_1():
    global ans, count
    ans = []
    ans = s1 + list(s2[n - 1])
    point = n - 1
    for i in range(n):
        if s1[i] == '1' and s2[i - 1] == '0' and (i - 1 >= 0):
            ans = s1[0:i]
            ans = ans + s2[i - 1:n]
            point = i - 1
            break
    count = 1
    for i in range(point, -1, -1):
        if s1[i] != s2[i - 1]:
            break
        count = count + 1
t = int(input())
cnt = []
fin = []
for i in range(t):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
    func_1()
    cnt.append(count)
    fin.append(ans)
for i in range(t):
    print(''.join(fin[i]))
    print(cnt[i])
'\nt=int(input())\nfor i in range(t):\n    n=int(input())\n    a=[[0]*n for j in range(2)]\n    a[0]=[int(j) for j in list(input())]\n    a[1]=[int(j) for j in list(input())]\n    dp=[[0]*n for j in range(2)]\n    for j in range(n):\n        if j==0:\n            dp[0][j]=a[0][j]\n            dp[1][j]=dp[0][j]+a[1][j]\n        else:\n            dp[0][j]=dp[0][j-1]+a[0][j]\n            dp[1][j]=min(dp[0][j],dp[1][j-1])+a[1][j]\n    print(dp[1][n-1])\n'