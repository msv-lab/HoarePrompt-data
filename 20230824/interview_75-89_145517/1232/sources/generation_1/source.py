nA, nB = map(int, input().split())
k, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Check if the maximum number in A is strictly less than the minimum number in B
if A[k-1] < B[nB-m]:
    print("YES")
else:
    print("NO")