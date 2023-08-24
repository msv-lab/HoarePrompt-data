N, K = map(int, input().split())
A = list(map(int, input().split()))

MOD = 10**9 + 7

A.sort() # Sort the array in ascending order

ans = 0
for i in range(K-1, N):
  # To choose K elements, we take the difference between the maximum and minimum
  # element of the chosen subarray.
  # f(S) = max(S) - min(S)
  # To calculate f(S) efficiently, we subtract the minimum element from the maximum element
  # of a sliding window of size K. We keep updating the answer with this difference.
  ans = (ans + A[i] - A[N-i-1]) % MOD

print(ans)