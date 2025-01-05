INF = float("inf")

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(lambda y: int(y) - 1, input().split()))  # Convert to zero-based indexing
    dp1 = [[0] * (n + 1) for _ in range(n + 1)]  # DP table for subarray operations

    for r in range(n + 1):
        dp2 = [[0] * x for _ in range(r + 1)]  # DP table for subarray to specific value
        dp2[-1] = [1] * x  # Initialize with 1 operation for each possible value

        for l in reversed(range(r)):
            for k in range(x):
                # Calculate minimum operations for subarray a[l:r] to become k
                dp2[l][k] = min(dp2[l + 1][k], dp1[l + 1][r] + 1) if k != a[l] else INF

            for c in range(l + 1, r):
                # Update dp2 considering the subarray a[l:c] and a[c:r]
                dp2[l][a[c - 1]] = min(dp2[l][a[c - 1]], dp1[l][c] + dp2[c][a[c - 1]])

            # Update dp1 for subarray a[l:r]
            dp1[l][r] = min(dp2[l][k] for k in range(x))

    result = INF

    for k in range(x):
        dp3 = [INF] * (n + 1)  # DP table for making the whole array equal to k
        dp3[0] = 0  # No operation needed for empty subarray

        for i in range(n):
            if a[i] == k:
                dp3[i + 1] = min(dp3[i + 1], dp3[i])  # No operation needed if already k

            for j in range(i + 1, n + 1):
                # Update dp3 considering subarray a[i:j]
                dp3[j] = min(dp3[j], dp3[i] + dp1[i][j])

        # Find the minimum operations for any target value k
        result = min(result, dp3[-1])

    print(f'{result}')