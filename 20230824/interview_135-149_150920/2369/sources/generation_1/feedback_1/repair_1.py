N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7

ans = 0
for i in range(N-K+1):
  # To choose K elements, we take the difference between the maximum and minimum
  # element of the chosen subarray.
  # f(S) = max(S) - min(S)
  # To calculate f(S) efficiently, we subtract the minimum element from the maximum element
  # of a sliding window of size K. We keep updating the answer with this difference.
  ans = (ans + max(A[i:i+K]) - min(A[i:i+K])) % MOD

print(ans)