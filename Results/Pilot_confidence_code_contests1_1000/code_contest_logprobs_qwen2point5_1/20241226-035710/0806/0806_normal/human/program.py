#coding:utf-8

n=input()
A=map(int, raw_input().split(" "))
A.sort()
ans=A[0]
for a in A[1:]:
    m=a%ans
    if m!=0:
        ans=min(m,ans)
print(ans)