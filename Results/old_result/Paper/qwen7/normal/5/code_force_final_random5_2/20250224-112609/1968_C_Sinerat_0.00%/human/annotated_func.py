#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, and x is a list of n-1 integers such that 1 ≤ x_i ≤ 500 for all 2 ≤ i ≤ n.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: Output State: After the loop executes all its iterations, the list `a` will contain `n` elements. The first element `a[0]` is 500, and each subsequent element `a[i]` (for \(0 \leq i < n\)) will be the sum of 500 and the cumulative sum of the first \(i+1\) elements of the list `x`. In other words, `a[i]` will be equal to `500 + sum(x[:i+1])`. The final element `a[n-1]` will be the sum of 500 and the cumulative sum of all elements in the list `x`.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer `n` and a list `x` of `n-1` integers. It then calculates a list `a` where the first element is 500, and each subsequent element is the cumulative sum of 500 and the first `i+1` elements of `x`. Finally, it prints the list `a` for each test case.

