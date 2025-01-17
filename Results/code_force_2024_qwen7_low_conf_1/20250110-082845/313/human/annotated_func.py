#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and k are positive integers such that 1 ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^{15}. a is a list of n positive integers such that 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 2⋅10^5.
def func():
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, k = R()
        
        *a, = R()
        
        i = 0
        
        j = n - 1
        
        while i < j and (m := min(a[i], a[j], k // 2)):
            k -= m * 2
            a[i] -= m
            i += a[i] < 1
            a[j] -= m
            j -= a[j] < 1
        
        print(i + n - j - 1 + (k >= a[i] > 0))
        
    #State of the program after the loop has been executed: t` is 0, `n` is the value returned by `R()` after the loop, `k` is 0, `a` is an empty list, and the printed value is `i + n - j - 1 + (k >= a[i] > 0)
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer \( t \) (number of test cases), two integers \( n \) and \( k \) (where \( 1 \leq n \leq 2 \times 10^5 \) and \( 1 \leq k \leq 10^{15} \)), and a list \( a \) of \( n \) positive integers (where \( 1 \leq a_i \leq 10^9 \)). For each test case, it repeatedly adjusts the values in list \( a \) by subtracting a value \( m \) (determined as the minimum of \( a[i] \), \( a[j] \), and \( k // 2 \)) from both ends of the list until either \( i \geq j \) or \( m \) becomes zero. Finally, it prints the number of elements in the list that have a non-zero value plus one if \( k \) is still greater than or equal to the remaining element \( a[i] \). The function implicitly returns nothing, but the printed value represents the result for each test case.

