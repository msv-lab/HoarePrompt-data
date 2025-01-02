# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
N,K = map(int, input().split())
S =set()
for _ in range(K):
    l,r = map(int, input().split())
    S |=set(list(range(l,r+1)))
S =list(S)
S.sort()
DP =[0]*(N+1)
DP[1] =1
for i in range(1,N+1):
    for s in S:
        if i +s <=N:
            DP[i+s] +=DP[i]
        else:
            break
ans =DP[N] %998244353 
print(ans)