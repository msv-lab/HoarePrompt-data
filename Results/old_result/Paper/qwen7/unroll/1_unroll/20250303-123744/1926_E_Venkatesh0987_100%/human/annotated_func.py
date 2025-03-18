#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        s = 0
        
        i = 0
        
        d = n
        
        h = n
        
        p = 1
        
        g = 0
        
        if k > (n + 1) // 2:
            while s < k and d > 0:
                s += (d + 1) // 2
                d -= (d + 1) // 2
                i += 1
            while p <= i - 1:
                g += (h + 1) // 2
                h -= (h + 1) // 2
                p += 1
            f = k - g
            y = 2 ** (i - 1) * (2 * f - 1)
            print(y)
        else:
            print(2 * k - 1)
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 5 ⋅ 10^4. For each test case, n and k are integers such that 1 ≤ k ≤ n ≤ 10^9. After all the executions of the loop have finished, the values of n and k from each test case will be processed according to the given conditions, and the result (a single integer value calculated for each test case) will be printed. The variables `s`, `i`, `d`, `h`, `p`, `g`, and `f` will be reset to their initial values before processing the next test case.
#Overall this is what the function does:The function processes multiple test cases, each containing integers \( t \), \( n \), and \( k \). For each test case, it calculates and prints a specific integer value based on the given conditions. If \( k \) is greater than half of \( n + 1 \), it performs a series of calculations involving variables \( s \), \( d \), \( h \), \( p \), and \( g \) to determine the final output. Otherwise, it directly prints \( 2k - 1 \). After processing each test case, it resets the relevant variables before moving on to the next case.

