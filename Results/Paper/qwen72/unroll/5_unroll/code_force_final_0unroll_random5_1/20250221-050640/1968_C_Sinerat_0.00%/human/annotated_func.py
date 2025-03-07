#State of the program right berfore the function call: The function `func` should accept a list of integers `x` where `1 <= len(x) <= 500` and `1 <= x_i <= 500` for all `2 <= i <= n`. Additionally, the function should handle multiple test cases, where the number of test cases `t` is an integer such that `1 <= t <= 10^4`. The sum of values `n` over all test cases does not exceed `2 * 10^5`.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        x = list(map(int, input().split()))
        
        a = [0] * n
        
        a[0] = 500
        
        for i in range(1, n):
            a[i] = a[i - 1] + x[i - 1]
        
        print(*a)
        
    #State: For each test case, the function prints a list `a` where the first element is 500, and each subsequent element is the cumulative sum of the elements from the input list `x` up to that index, starting from the first element of `x`. The variables `t` and `x` remain unchanged, and `n` and `a` are reset for each new test case.
#Overall this is what the function does:The function `func` processes multiple test cases, where each test case involves a list of integers `x`. For each test case, it generates a new list `a` where the first element is always 500, and each subsequent element is the cumulative sum of the elements from the input list `x` up to that index. The function prints the list `a` for each test case. The input variables `t` and `x` remain unchanged, and the variables `n` and `a` are reset for each new test case.

