#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and s is a binary string with 2 ≤ |s| ≤ 2 · 10^5, where each character in s is either '0' or '1'. The sum of the lengths of all strings across all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `s` is a list of integers representing the digits of the final input string, `n` is 0 (indicating the loop has completed its iterations), `zeroes` is the number of times 0 appears in the final list `s`, `cnt` is `[zeroes, len(s) - zeroes]`, and `ans` is the sum of the number of times a 1 appears before each 0 in the final list `s` plus the total number of 0s multiplied by the number of 1s.
#Overall this is what the function does:The function `func_1` reads an integer `n` indicating the number of test cases. For each test case, it reads a binary string `s` and calculates the sum of the number of times a '1' appears before each '0' in the string, plus the total number of '0's multiplied by the number of '1's. It prints the result for each test case. After processing all test cases, the function completes, and the state includes `n` being 0 (indicating the loop has completed), `s` being the last processed binary string as a list of integers, `zeroes` being the count of '0's in `s`, `cnt` being a list with the counts of '0's and '1's in `s`, and `ans` being the calculated result for the last test case.

