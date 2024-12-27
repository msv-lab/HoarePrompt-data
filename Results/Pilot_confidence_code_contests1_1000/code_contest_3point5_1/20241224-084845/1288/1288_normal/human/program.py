import sys
import math
n = int(input())
k=0
m={}
maxi=0
for i in range(0,n):
    s = raw_input()
    if not s in m :
        m[s]=1;
        k+=1;
    else :
        m[s]+=1;
    if maxi < m[s]:
        maxi = m[s]
        str = s
print(s)
sys.exit()