#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a binary string such that 2 ≤ |s| ≤ 2 ⋅ 10^5 and s_i ∈ {0, 1}.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `ans` is the sum of counts calculated from the loop executions for each input list `s`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a binary string `s`. For each test case, it calculates and prints a value `ans` based on the count of zeros and ones in the string. Specifically, `ans` is determined by comparing the number of zeros and ones encountered so far in the string.

