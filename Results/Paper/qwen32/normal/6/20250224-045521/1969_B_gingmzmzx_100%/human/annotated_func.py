#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. Each of the following t lines contains a binary string s such that 2 <= |s| <= 2 * 10^5 and the sum of lengths of all strings s over all test cases does not exceed 2 * 10^5.
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
        
    #State: The final `ans` value calculated from the last binary string `s` read in the `n`-th iteration.
#Overall this is what the function does:The function `func_1` processes a series of binary strings, each representing a test case. For each binary string, it calculates a value based on the number of 0s and 1s in the string and prints this value. The function handles up to 10,000 test cases, with each binary string having a length between 2 and 200,000 characters, and the total length of all binary strings not exceeding 200,000 characters.

