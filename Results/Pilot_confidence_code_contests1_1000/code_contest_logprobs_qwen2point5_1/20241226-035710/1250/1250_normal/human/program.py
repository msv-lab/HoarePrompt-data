import math
import sys
input=sys.stdin
write=sys.stdout.write
n=int(input.readline())
s=input.readline().split()
x1,x2=int(s[0]),int(s[1])
B=[]
C=[]
for i in range(n):
    s=input.readline().split()
    k,b=int(s[0]),int(s[1])
    B.append([k*x1+b,k*x2+b])
B.sort(key=lambda x:x[0]*10*15+x[1])
c='No'
for i in range(n-1):
    if B[i+1][0]!=B[i][0]:
        if B[i+1][1]<B[i][1]:
            c='Yes'
write(c)
           
