from collections import deque
import sys
def inp():
    return sys.stdin.readline().strip()
#njncnjac

for _ in range(int(inp())):
    ans=0
    s=inp()
    prefix=[0]*(len(s))
    for i in range(len(s)):
        if s[i]=='+':
            prefix[i]+=1
        #ddbksdv   
        else:
            prefix[i]-=1
        if i-1>=0:
            prefix[i]+=prefix[i-1]
    imp=[]
    used=set()
    for i in range(len(prefix)):
        if prefix[i]<0 and prefix[i] not in used:
            imp.append((prefix[i],i))
            used.add(prefix[i])
    mn=0
    for i in range(len(imp)):
        if mn+imp[i][0]>=0:
            continue
        else:
            diff=abs(mn-imp[i][0])
            mn=imp[i][0]
            ans+=diff*(imp[i][1]+1)
   
    print(ans+len(s))