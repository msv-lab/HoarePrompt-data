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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, `ans` is the sum of counts calculated from the input lists `s` after executing the loop for `n` times. Each `ans` value is determined based on the counts of 0s and 1s in the list `s` for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it calculates and prints a value `ans` based on the counts of 0s and 1s in the binary string `s`. If `t` is within the range 1 to 10^4, it performs the calculation; otherwise, it does not process the test case. The final output consists of `t` lines, each containing the calculated value `ans` for the respective test case.

