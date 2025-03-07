class Solution:
    def Coins(self, n: int, s: str) -> int:
        if n == 0:
            return 0
        
        dp = [0] * n
 
        if s[0] == '@':
            dp[0] = 1
 
        if n > 1 and s[1] != '*':
            dp[1] = dp[0] + (1 if s[1] == '@' else 0)
 
        for i in range(2, n):
            if s[i] != '*':
                dp[i] = max(dp[i-1], dp[i-2])
                if s[i] == '@':
                    dp[i] += 1
 
        return dp[-1]
 
solution = Solution()
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = input()
    print(solution.Coins(n, a))