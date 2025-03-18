#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, s is a binary string (a string consisting of only '0's and '1's) with length 2 ≤ |s| ≤ 2 · 10^5. The sum of the lengths of all strings s over all test cases does not exceed 2 · 10^5.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4, s is the last binary string processed as a list of integers, n is 0, zeroes is the count of 0s in the last binary string, cnt is [number of 0s in the last binary string, number of 1s in the last binary string], ans is the accumulated value of valid (0, 1) pairs across all iterations.
#Overall this is what the function does:The function `func_1` reads an integer `n` representing the number of test cases, and for each test case, it reads a binary string `s`. It then calculates and prints the number of valid (0, 1) pairs in the string `s`, where a valid pair is defined as a '0' that appears before any '1'. This process is repeated for each of the `n` test cases.

