def lps(s: str) -> int:
    n = len(s)
    # Create a 2D array to store the length of the longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]
    
    # All substrings of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Build the table. Note that the bottom-up approach is used here.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    # The length of the longest palindromic subsequence is in dp[0][n-1]
    return dp[0][n - 1]

# Test cases
assert lps("TENS FOR TENS") == 5
assert lps("CARDIO FOR CARDS") == 7
assert lps("PART OF THE JOURNEY IS PART") == 9
