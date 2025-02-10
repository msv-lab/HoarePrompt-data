#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(range(1, n + 1))
        
        for i in range(n // 2):
            a[2 * i + 1] = n - i
            a[2 * i] = i + 1
        
        if len(a) % 2 == 1:
            a[n - 1] = n // 2 + 1
        
        print(*a)
        
    #State: Output State: The final output state after the loop executes all its iterations is a list `a` where for each `i` from 0 to `n // 2 - 1`, `a[2 * i]` equals `i + 1` and `a[2 * i + 1]` equals `n - i`. If the length of `a` is odd, the last element `a[n - 1]` equals `n // 2 + 1`. All other elements of `a` remain unchanged.
    #
    #This means that after the loop completes all its iterations, the list `a` will be structured as follows:
    #- For even `n`, the list will be `[1, n, 3, n-1, 5, n-2, ..., n//2, n//2]`.
    #- For odd `n`, the list will be `[1, n, 3, n-1, 5, n-2, ..., n//2+1, n//2+1]`.
    #
    #The length of `a` will always be equal to `n`, and the specific values of `a` will depend on the value of `n` as described above.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers \( t \) and \( n \). For each test case, it constructs a list \( a \) of length \( n \) based on the value of \( n \). If \( n \) is even, the list is structured as \([1, n, 3, n-1, 5, n-2, \ldots, n/2, n/2]\). If \( n \) is odd, the list is structured as \([1, n, 3, n-1, 5, n-2, \ldots, (n+1)/2, (n+1)/2]\). The function then prints the constructed list for each test case.

