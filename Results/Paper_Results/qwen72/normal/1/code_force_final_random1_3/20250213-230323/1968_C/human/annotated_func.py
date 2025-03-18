#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 2 ≤ n ≤ 500, representing the number of elements in the array a. The array x contains n-1 integers x_2, ..., x_n, where 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: After all iterations of the loop, `t` is an integer such that 1 ≤ t ≤ 10^4, and for each of the `t` test cases, `n` is an integer such that 2 ≤ n ≤ 500, `x` is a list of `n-1` integers provided by the user, and `a` is a list of length `n` where `a[0]` is 1000, and for each index `i` from 1 to `n-1`, `a[i]` is the sum of `a[i-1]` and `x[i-1]`. The loop has completed all `t` iterations, and the final state of `a` for each test case is printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by an integer `n` and a list `x` of `n-1` integers. For each test case, it constructs a list `a` of length `n` where the first element is always 1000, and each subsequent element is the sum of the previous element in `a` and the corresponding element in `x`. The function prints the list `a` for each test case. After processing all test cases, the function completes without returning any value.

