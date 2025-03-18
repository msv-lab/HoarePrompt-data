#State of the program right berfore the function call: The function `func` is expected to process multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 500) representing the number of elements in the array `a`, and a list of `n-1` integers `x` (1 ≤ x_i ≤ 500) representing the elements of the array `x`. The number of test cases `t` is a positive integer (1 ≤ t ≤ 10^4). The sum of values `n` over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 1000
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the array `a` will contain `n` elements where `a[0]` is 1000, and each subsequent element `a[i]` (for 1 ≤ i < n) is the cumulative sum of the previous element `a[i-1]` and the corresponding element `x[i-1]` from the input list `x`. The values of `t`, `n`, and `x` will remain unchanged as they are input variables.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n-1` integers `x`. It then constructs an array `a` of `n` elements where `a[0]` is set to 1000, and each subsequent element `a[i]` (for 1 ≤ i < n) is the cumulative sum of the previous element `a[i-1]` and the corresponding element `x[i-1]`. The function prints the elements of `a` for each test case. The input variables `t`, `n`, and `x` remain unchanged.

