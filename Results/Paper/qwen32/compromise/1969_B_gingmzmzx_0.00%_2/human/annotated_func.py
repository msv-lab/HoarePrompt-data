#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, s is a binary string of length between 2 and 2 * 10^5 inclusive, consisting only of '0' and '1'. The sum of the lengths of all strings across all test cases does not exceed 2 * 10^5.
def func_1():
    n = int(input())
    for _ in range(n):
        s = list(map(int, input().strip()))
        
        zeroes = s.count(0)
        
        cnt = [0, 0]
        
        ans = 0
        
        for c in s:
            cnt[c] += 1
            if c == 0:
                ans += 1 if cnt[1] > 0 else 0
            else:
                ans += zeroes - cnt[0]
        
        print(ans)
        
    #State: t remains the same, n becomes 0, cnt contains the total counts of 0s and 1s, ans contains the accumulated result.
#Overall this is what the function does:The function `func_1` processes `t` test cases, where each test case consists of a binary string `s`. For each binary string, it calculates and prints a value `ans` which represents the number of valid pairs `(i, j)` such that `i < j` and the substring `s[i:j+1]` contains at least one '0' and one '1'.

