#State of the program right berfore the function call: The input consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 100) representing the length of the string, and the second line contains a string s consisting of n lowercase Latin letters.
def func():
    n = int(input())

s = input()

dp = [0] * (n + 1)

dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = i
        
        for j in range(i):
            if s[j:i] in s[:j]:
                dp[i] = min(dp[i], dp[j] + (i - j) // (i - j - j) + 1)
        
    #State of the program after the  for loop has been executed: `i` is `n + 3`, `dp` is updated based on the condition inside the loop, `n` must be greater than or equal to 1, and `s` is a string consisting of `n` lowercase Latin letters.
    print(dp[n])
#Overall this is what the function does:The function reads an integer \( n \) and a string \( s \) consisting of \( n \) lowercase Latin letters. It then computes and prints the minimum number of deletions required to make the string \( s \) such that no substring of length greater than 1 repeats consecutively. If the input does not meet the specified constraints (e.g., \( n \) is less than 1), the function will handle these cases appropriately. Edge cases include when \( n = 1 \) (in which case no deletions are needed), and when the string \( s \) already meets the criteria (no repeated substrings of length greater than 1). The function uses dynamic programming to achieve this, where \( dp[i] \) represents the minimum number of deletions required for the first \( i \) characters of \( s \).

