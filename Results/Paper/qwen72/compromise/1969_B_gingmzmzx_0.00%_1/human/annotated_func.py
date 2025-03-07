#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and s is a binary string (2 ≤ |s| ≤ 2 · 10^5, s_i ∈ {0, 1}) for each test case. The sum of the lengths of strings over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `s` is a list of integers where each element is either 0 or 1, `n` is 0, `zeroes` is the number of 0s in the final `s`, `cnt` is [number of 0s in the final `s`, number of 1s in the final `s`], `ans` is the sum of the number of 1s before each 0 in the final `s` plus the product of the number of 0s and the number of 1s in the final `s`.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads a binary string `s` and calculates a value `ans`. This value is computed based on the positions of 0s and 1s in the string, specifically counting the number of 1s before each 0 and the total number of 0s and 1s in the string. The function prints the calculated value `ans` for each test case. After processing all test cases, the function concludes, and the final state includes `n` being 0, `s` being a list of integers representing the last processed binary string, and `ans` being the last calculated value.

