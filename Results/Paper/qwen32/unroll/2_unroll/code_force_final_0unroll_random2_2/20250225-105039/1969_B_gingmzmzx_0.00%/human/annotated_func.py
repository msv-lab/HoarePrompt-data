#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, s is a binary string of length between 2 and 2 * 10^5, inclusive. The sum of the lengths of all strings s across all test cases does not exceed 2 * 10^5.
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
        
    #State: The printed values of `ans` for each of the `n` test cases.
#Overall this is what the function does:The function `func_1` processes a series of binary strings, each representing a test case. For each string, it calculates a value based on the positions of '0's and '1's and prints this value. The printed value for each test case represents the number of valid pairs of indices (i, j) such that i < j and the substring s[i:j+1] contains at least one '0' and one '1'.

