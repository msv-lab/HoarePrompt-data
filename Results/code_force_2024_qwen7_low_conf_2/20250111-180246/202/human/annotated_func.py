#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and s is a binary string of length n.
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
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^4\), `n` is an integer such that \(1 \leq n \leq 2 \cdot 10^5\) and remains unchanged, `s` is a binary string of length `n` and remains unchanged, `mn` is the overall minimum value that `cur` attains across all iterations of the loop, `mx` is the overall maximum value that `cur` attains across all iterations of the loop, `cur` is 0, and the value printed is `mx - mn`.
#Overall this is what the function does:The function processes multiple test cases, each including an integer `t` (1 ≤ t ≤ 10^4), an integer `n` (1 ≤ n ≤ 2⋅10^5), and a binary string `s` of length `n`. For each test case, it calculates the difference between the maximum and minimum values of a variable `cur`, which changes based on the parity of the cumulative sum of the binary string `s`. Specifically, `cur` increases by 1 if the current character in `s` maintains the parity of the sum, and decreases by 1 otherwise. The function prints the difference between the maximum and minimum values of `cur` for each test case. After processing all test cases, the function does not return any value.

