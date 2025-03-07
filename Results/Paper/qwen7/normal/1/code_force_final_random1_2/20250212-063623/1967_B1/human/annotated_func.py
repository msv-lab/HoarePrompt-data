#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: `count` is `m + 1`, `countmins` is `m`, `g` is `0`, `ans` is the sum of `n` plus the series of increments calculated from all loop iterations, `i` is `t`, `m` is the final value of `m` from the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates and prints a value based on \( n \) and the number of iterations up to \( m \). Specifically, it iteratively updates a running total starting from \( n \), adding a calculated increment in each iteration until the specified limit \( m \) is reached. The final printed value represents the sum of the initial \( n \) and all the increments calculated during the iterations.

