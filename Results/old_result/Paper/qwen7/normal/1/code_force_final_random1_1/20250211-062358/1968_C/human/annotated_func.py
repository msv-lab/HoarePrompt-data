#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: The list `a` will be a list of length `n` with the first element being 1000, and each subsequent element being the cumulative sum of 1000 plus the sum of all elements in `x` up to that point.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `x` of `n-1` integers. For each test case, it calculates a list `a` of length `n`, where the first element is set to 1000, and each subsequent element is the cumulative sum of 1000 plus the sum of all preceding elements in `x`. The function prints the list `a` for each test case.

