import sys
sys.setrecursionlimit(int(1e7+5))

n = int(raw_input())
w = [0]*n
s = [0]*n
v = [0]*n

for i in range(n):
    w[i], s[i], v[i] = list(map(int, raw_input().split()))
    
a = []
for i in range(n):
    a.append((w[i], s[i], v[i]))



def compare(p, q):
    return p[0]+p[1]-q[0]-q[1]
    # if (p[0]>q[0]):
    #     return 1
    # elif (p[0]<q[0]):
    #     return -1;
    # else:
    #     return p[1]-q[1]

a.sort(cmp=compare)

w = [x[0] for x in a]
s = [x[1] for x in a]
v = [x[2] for x in a]

dp = [[-1]*(10000+1) for i in range(1000+1)]

def solve(i, wsum):
    if (i==n):
        return 0
    if wsum>1e4:
        return 0
    
    if (dp[i][wsum]!=-1):
        return dp[i][wsum]

    ans = 0

    if s[i]>=wsum:
        ans = max(ans, v[i]+solve(i+1, wsum+w[i]))
        ans = max(ans, solve(i+1, wsum))
    else:
        ans = max(ans, solve(i+1, wsum))

    dp[i][wsum]=ans
    return ans

print(solve(0, 0))
        