#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and s is a binary string of length n. The sum of n over all test cases does not exceed 2⋅10^5.
def func_1():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        mn = 0
        
        mx = 0
        
        cur = 0
        
        for c in s:
            if (cur % 2 == 0) == (c == '1'):
                cur = cur + 1
            else:
                cur = cur - 1
            mn = min(mn, cur)
            mx = max(mx, cur)
        
        print(mx - mn)
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases, `n` is an integer read from input, `s` is a binary string of length `n` read from input, `cur` is an integer that is the final value of `cur` after processing all characters in `s`, `mx` is the maximum value of `cur` encountered during the loop, `mn` is the minimum value of `cur` encountered during the loop, and the printed value is `mx - mn`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \(t\) representing the number of binary strings to process, followed by \(t\) pairs of integers \(n\) and a binary string \(s\) of length \(n\). For each binary string, the function calculates and prints the difference between the maximum and minimum values of a running count `cur`. The running count `cur` increments by 1 if the current character in the binary string matches the parity of its index, otherwise it decrements by 1. The function handles up to \(10^4\) test cases, with each binary string having a length between 1 and \(2 \cdot 10^5\), and ensures that the total length of all strings does not exceed \(2 \cdot 10^5\).

