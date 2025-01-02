N = input()
D,X = map(int, raw_input().split())
A = []
for i in range(N):
    A.append(input())
ans = 0
for i in range(N):
    t = ((D-1) / A[i]) + 1
    ans += t
ans += X
print(ans)