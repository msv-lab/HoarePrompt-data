#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n values across all test cases does not exceed 10^5.
def func():
    for i in range(int(input())):
        n = [int(i) for i in input().split()][0]
        
        p = [0] * n
        
        ind = n
        
        for i in range(0, n, 2):
            p[i] = ind
            ind -= 2
        
        ind = 1 + n % 2
        
        for i in range(1, n, 2):
            p[i] = ind
            ind += 2
        
        print(*p)
        
    #State: Output State: For each test case, the output is a list `p` of length `n`, where the elements at even indices are filled with decreasing even numbers starting from `n` down to 2, and the elements at odd indices are filled with increasing even numbers starting from 1 up to `n-1` if `n` is odd, or `n+1` if `n` is even.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( n \) (where \( 3 \leq n \leq 10^5 \)). For each \( n \), it constructs a list \( p \) of length \( n \) where the elements at even indices are filled with decreasing even numbers starting from \( n \) down to 2, and the elements at odd indices are filled with increasing even numbers starting from 1 up to \( n-1 \) if \( n \) is odd, or \( n+1 \) if \( n \) is even. The function then prints the list \( p \) for each test case.

