#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. Additionally, the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: `ans` is the sum of `n` and the series `n / 2 - 1 / 2 + 1`, `((n / 3) - 1) / 3 + 1`, ..., `((n / m) - 1) / m + 1`, `count` is `m + 1`, `countmins` is `m - 1`, and `g` is `n / m - m - 1`
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates a value based on \( n \) and \( m \) using a specific formula and prints the result. The function ensures that the input values meet certain constraints (i.e., \( 1 \leq t \leq 10^4 \), \( 1 \leq n, m \leq 2 \cdot 10^6 \), and the sum of \( n \) and \( m \) does not exceed \( 2 \cdot 10^6 \)). After processing all test cases, the function prints the calculated value for each case.

