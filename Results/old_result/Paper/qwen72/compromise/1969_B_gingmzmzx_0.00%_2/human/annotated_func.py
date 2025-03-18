#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, and for each test case, s is a binary string with 2 ≤ |s| ≤ 2 · 10^5, and the sum of lengths of strings over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `s` is a list of integers representing the digits of the final input binary string, `n` is 0, `zeroes` is the count of zeros in the list `s`, `cnt` is [number of 0s in `s`, number of 1s in `s`], `ans` is the sum of the number of 1s in `s` multiplied by the total number of zeros in `s` minus the cumulative count of 0s encountered up to each 1.
#Overall this is what the function does:The function `func_1` reads an integer `t` indicating the number of test cases, where `1 ≤ t ≤ 10^4`. For each test case, it reads a binary string `s` (2 ≤ |s| ≤ 2 · 10^5) and calculates a value `ans` based on the positions of '0's and '1's in the string. Specifically, for each '1' in the string, it adds the number of '0's that come after it in the string to `ans`. The function prints the calculated `ans` for each test case. After processing all test cases, the function ends, and the state is such that `t` remains unchanged, `s` is the last processed binary string converted to a list of integers, `n` is 0, `zeroes` is the count of zeros in the last `s`, `cnt` is the count of '0's and '1's in the last `s`, and `ans` is the final calculated value for the last test case.

