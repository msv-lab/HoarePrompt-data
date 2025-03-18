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
        
    #State: Output State: t test cases where for each test case, n is the number of elements in the list x, and a is a list of n integers. The first element of a is always 1000, and each subsequent element is the sum of the previous element and the corresponding element from the list x.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (number of elements in the list `x`), and a list `x` of `n-1` integers. It then creates a list `a` of length `n`, sets the first element to 1000, and calculates each subsequent element as the sum of the previous element and the corresponding element from list `x`. Finally, it prints the list `a` for each test case.

