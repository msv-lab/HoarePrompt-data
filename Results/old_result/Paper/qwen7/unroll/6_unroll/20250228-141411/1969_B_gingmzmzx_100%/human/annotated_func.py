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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an input integer, and for each input list `s`, `ans` is calculated based on the given logic and printed after all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes an integer `t` (number of binary strings) and a binary string `s`. For each binary string `s`, it calculates and prints a value `ans` based on the count of zeros and ones in the string. Specifically, `ans` is determined by counting the number of positions where a zero is followed by a one or vice versa, according to the given logic. After processing all test cases, the function outputs the calculated values for each test case.

