n = input()
A = [raw_input() for i in xrange(n)]

R = [sum(e[j] == '#' for j in xrange(n)) for e in A]
C = [sum(A[j][i] == '#' for j in xrange(n)) for i in xrange(n)]

c_need = sum(e < n for e in C)

INF = 10**9+7
ans = INF
for i in xrange(n):
    if R[i] == C[i] == 0:
        continue
    if C[i] == 0:
        ans = min(ans, n-R[i] + c_need + 1)
    else:
        ans = min(ans, n-R[i] + c_need)
print -1 if ans == INF else ans
