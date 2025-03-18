#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a binary string such that 2 ≤ |s| ≤ 2 \cdot 10^5 and s_i ∈ {0, 1}.
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
        
    #State: Output State: After all iterations of the loop, `ans` will be the sum of the number of zeros in the list `s` plus the count of ones in `s` minus 1, `cnt` will contain the count of each integer in `s`, `zeroes` will be the initial number of zeros in `s`, `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is the number of times the loop was executed, and `s` is a list of integers that has been fully processed.
    #
    #In natural language, after the loop completes all its iterations, `ans` will be calculated as follows: for each '0' in the list `s`, add 1 to `ans` if there has been at least one '1' encountered so far (tracked by `cnt[1]`); for each non-zero element, add the initial number of zeros (`zeroes`) minus the count of zeros seen so far (`cnt[0]`) to `ans`. The variable `cnt` will hold the total counts of each integer in `s`, `zeroes` will still hold the initial count of zeros in `s`, `t` will remain unchanged as it is not affected by the loop, and `n` will be the final value of the loop counter, indicating how many times the loop ran.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `t` and a binary string `s`. For each test case, it calculates a value `ans` based on the counts of zeros and ones in the string `s`. Specifically, `ans` is computed as the sum of the number of zeros in `s` plus the count of ones in `s` minus 1. The function prints `ans` for each test case and does not return any value.

