#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each of the t test cases, there is a binary string s such that 2 <= |s| <= 2 * 10^5, and the sum of lengths of all strings s over all test cases does not exceed 2 * 10^5.
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
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of a binary string. For each binary string, it calculates and prints a value based on the number of 1s that appear after each 0 in the string. Specifically, for each 0 in the string, it counts how many 1s have appeared before it, and for each 1, it counts how many 0s have not yet appeared. The function outputs this calculated value for each test case.

