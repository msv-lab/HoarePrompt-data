def min_removal_subsequence(a, b):
    # dp[i][j] will be the length of longest common subsequence of a[0:i] and b[0:j]
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # Fill dp array
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the longest common subsequence from the dp table
    i, j = len(a), len(b)
    lcs = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    lcs_string = ''.join(lcs)

    # If the LCS is empty, return "-"
    if not lcs_string:
        return "-"
    else:
        return lcs_string

# Read input
a = input().strip()
b = input().strip()

# Compute and print the result
print(min_removal_subsequence(a, b))
