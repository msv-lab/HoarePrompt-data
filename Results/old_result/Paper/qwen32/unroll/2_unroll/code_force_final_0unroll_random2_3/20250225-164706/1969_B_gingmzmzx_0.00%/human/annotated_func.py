#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, s is a binary string of length between 2 and 2 * 10^5, inclusive, consisting only of the characters '0' and '1'. The sum of the lengths of all strings s across all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4, and for each of the t test cases, `s` is a binary string of length between 2 and 2 * 10^5, inclusive, consisting only of the characters '0' and '1'. The sum of the lengths of all strings `s` across all test cases does not exceed 2 * 10^5; `n` is an input integer.
#Overall this is what the function does:The function `func_1` processes a series of binary strings, each representing a test case. For each binary string, it calculates a specific value based on the arrangement of '0's and '1's in the string and prints this value. The function handles multiple test cases, where the total number of test cases is provided as input, and the length of each binary string is between 2 and 200,000 characters.

