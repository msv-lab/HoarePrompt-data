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
        
    #State: Output State: `ind` is `2*n - 1`, `i` is `n`, and `p` is a list of length `n` where `p[i]` is `2*n - 1` for all `i` in the range `0` to `n-1`.
    #
    #In natural language: After the loop has executed all its iterations, the value of `ind` will be `2*n - 1`. The variable `i` will be equal to `n`. The list `p` will be filled with the value `2*n - 1` for every index from `0` to `n-1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) (where \( 3 \leq n \leq 10^5 \)). For each test case, it creates a list \( p \) of length \( n \) and fills it with the value \( 2n - 1 \). After processing all test cases, it prints the list \( p \) for each test case. The function does not return any value but outputs the final state of the list \( p \) for each test case.

