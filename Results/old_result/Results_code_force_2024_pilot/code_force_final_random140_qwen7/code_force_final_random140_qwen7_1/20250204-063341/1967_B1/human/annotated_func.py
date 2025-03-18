#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6, and the sum of all n and the sum of all m over all test cases do not exceed 2 \cdot 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: Output State: After the loop executes all its iterations, `b` will be equal to `min(n, m) + 1`, and `ans` will be the sum of `n // b + 1` for each `b` from 1 to `min(n, m)`.
    #
    #In simpler terms, after the loop has completed all its iterations, the variable `b` will be set to the smallest value between `n` and `m` plus one. The variable `ans` will contain the total sum of `n // b + 1` for every integer value of `b` ranging from 1 up to and including `min(n, m)`.
#Overall this is what the function does:The function processes multiple test cases, each containing two positive integers \( n \) and \( m \). For each test case, it calculates the sum of \( n // b + 1 \) for every integer \( b \) ranging from 1 to the minimum of \( n \) and \( m \), inclusive. The function prints the result for each test case.

