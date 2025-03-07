class Solution:
    def Coins(self, n: int, s: str) -> int:
        res = 0
        i = 0
        while i < n:
            if s[i] == '@':
                res += 1
            if i + 1 < n and s[i + 1] != '*':
                i += 1
            elif i + 2 < n and s[i + 2] != '*':
                i += 2
            else:
                break
        return res
 
solution = Solution()
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = input()
    print(solution.Coins(n, a))