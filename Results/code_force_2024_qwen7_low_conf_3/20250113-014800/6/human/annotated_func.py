#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for t in range(int(input())):
        n, k = map(int, input().split())
        
        r = n
        
        if k >= n - 1:
            r = 1
        
        print(r)
        
    #State of the program after the  for loop has been executed: `t` is a positive integer such that 1 ≤ t ≤ 10^3, `n` and `k` are integers from inputs, and for each test case, `r` is 1 if `k` is greater than or equal to `n - 1`. Otherwise, `r` is equal to `n`, and the final value of `r` is printed for each test case.
#Overall this is what the function does:The function processes a series of test cases, where for each test case, it reads two integers \( n \) and \( k \). Based on the value of \( k \) relative to \( n - 1 \), it sets the variable \( r \) to either 1 or \( n \). Specifically, if \( k \) is greater than or equal to \( n - 1 \), \( r \) is set to 1; otherwise, \( r \) is set to \( n \). The function then prints the value of \( r \) for each test case. The function handles up to 1000 test cases, with \( n \) ranging from 1 to 100 and \( k \) ranging from 0 to \(\frac{n \times (n - 1)}{2}\). Potential edge cases include when \( n \) is 1, in which case \( r \) will always be 1 regardless of \( k \).

