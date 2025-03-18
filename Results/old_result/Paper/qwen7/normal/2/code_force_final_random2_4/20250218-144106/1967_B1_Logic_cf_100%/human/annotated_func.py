#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 \cdot 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: `ans` is the sum of `(n + b) // (b * b)` for all `b` in the range from 2 to the minimum of `n` and `m`, inclusive, and `b` equals the minimum of `n` and `m`.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \( n \) and \( m \). For each test case, it calculates the sum of \((n + b) // (b * b)\) for all \( b \) in the range from 2 to the minimum of \( n \) and \( m \), and prints the result. If the input constraints are not satisfied, the function will not execute correctly.

