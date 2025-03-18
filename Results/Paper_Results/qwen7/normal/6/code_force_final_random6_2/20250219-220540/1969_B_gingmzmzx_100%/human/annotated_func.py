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
        
    #State: All elements in `s` have been processed for all iterations, `ans` contains the final calculated value based on the given conditions for all inputs, `zeroes` is the total number of zeros in all lists `s` across all iterations, `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is the total number of iterations, `cnt` is a dictionary where the keys are elements from the original lists `s` and the values are their respective counts in all lists `s` combined, and `c` is the last element in the last list `s` after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` and a binary string `s`. For each test case, it calculates and prints an integer `ans` based on the count of zeros and ones in the binary string `s`. The final output for each test case is the value of `ans`, which represents the number of valid subarrays under specific conditions.

