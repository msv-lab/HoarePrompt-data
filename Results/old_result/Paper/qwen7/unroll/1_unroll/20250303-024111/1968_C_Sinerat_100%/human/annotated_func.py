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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n. After executing the loop, a is a list of n integers where a[0] = 1000 and a[i] = a[i - 1] + x[i - 1] for all 1 ≤ i < n.
#Overall this is what the function does:The function processes a series of test cases. Each test case consists of an integer `t`, an integer `n`, and a list `x` of `n-1` integers. For each test case, it calculates a list `a` where `a[0] = 1000` and `a[i] = a[i - 1] + x[i - 1]` for all `1 ≤ i < n`. Finally, it prints the list `a` for each test case.

