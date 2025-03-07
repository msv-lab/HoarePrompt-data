#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, s is a binary string (a string consisting of only '0's and '1's) with length 2 <= |s| <= 2 * 10^5. The sum of the lengths of all strings s over all test cases does not exceed 2 * 10^5.
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
        
    #State: n printed values of `ans` for each binary string `s` processed.
#Overall this is what the function does:The function `func_1` processes a series of binary strings, each provided as input, and prints a value for each string. This value is determined based on the number of '1's that can be paired with '0's in the string, considering the order of characters. Specifically, for each '0' in the string, it counts how many '1's have appeared before it, and for each '1', it counts how many '0's will appear after it. The function does not return any value explicitly but prints the result for each binary string.

