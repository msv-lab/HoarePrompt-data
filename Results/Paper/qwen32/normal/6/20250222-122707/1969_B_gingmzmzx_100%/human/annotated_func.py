#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and for each test case, s is a binary string (a string consisting of only '0's and '1's) with length 2 <= |s| <= 2 * 10^5. The sum of lengths of all strings s over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop will have executed `n` times, and for each execution, it will have processed a binary string `s`. The variable `ans` will hold the accumulated score for the current binary string `s` after processing all its digits according to the rules specified in the loop. The variables `t` and `n` will remain unchanged from their initial values, as they are not modified within the loop.
#Overall this is what the function does:The function processes multiple binary strings, each representing a test case, and for each string, it calculates and prints a score based on the arrangement of '0's and '1's in the string.

