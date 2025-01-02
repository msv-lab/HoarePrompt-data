
N = [int(s) for s in raw_input().split(" ")][0]
A = [int(s) for s in raw_input().split(" ")]
B = [int(s) for s in raw_input().split(" ")]
C = [int(s) for s in raw_input().split(" ")]

res = 0
for i in xrange(N):
    res += B[A[i]-1]
    if i > 0 and A[i] == A[i-1]+1:
        print(C[i-1])
        res += C[A[i-1]-1]
print(res)