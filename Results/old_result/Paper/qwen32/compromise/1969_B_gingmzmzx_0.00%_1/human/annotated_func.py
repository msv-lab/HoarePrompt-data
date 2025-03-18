#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, s is a binary string (a string consisting of only '0's and '1's) with length 2 ≤ |s| ≤ 2 · 10^5. The sum of the lengths of all strings s over all test cases does not exceed 2 · 10^5.
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
        
    #State: The output state consists of `n` printed results, each representing the computed `ans` for each respective binary string `s`.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads a binary string `s` and computes a value `ans` based on the counts of '0's and '1's in the string. It then prints the computed `ans` for each test case.

