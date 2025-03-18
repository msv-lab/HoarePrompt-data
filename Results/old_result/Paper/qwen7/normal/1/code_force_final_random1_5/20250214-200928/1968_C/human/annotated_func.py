#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: `i` is `n`, `n` is an input integer, `a` is a list of length `n` where the first element is 1000, and each subsequent element is the sum of the previous element and the corresponding element from the list `x` (i.e., `a[i] = 1000 + sum(x[:i])`), `x` is a list of integers entered by the user.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( n \) (2 ≤ n ≤ 500) and a list \( x \) of \( n-1 \) integers (1 ≤ \( x_i \) ≤ 500 for all 2 ≤ i ≤ n). For each test case, it calculates a list \( a \) of length \( n \) where the first element is 1000, and each subsequent element is the cumulative sum of the previous element and the corresponding element from the list \( x \). The function then prints the elements of the list \( a \) for each test case.

